"""
Halaman Analisis
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

sys.path.append(str(Path(__file__).parent.parent))

from utils.data_loader import load_raw_data, preprocess_data
from utils.clustering import perform_clustering_all_years, get_cluster_summary
from config.settings import COLORS, CLUSTER_COLORS

# Import fungsi sidebar dari app.py
from app import render_sidebar

# MATIKAN FORMAT RIBUAN PANDAS
pd.options.display.float_format = '{:.0f}'.format

# Render sidebar yang konsisten
render_sidebar()

# Load data
@st.cache_data
def get_data():
    df_raw = load_raw_data()
    df = preprocess_data(df_raw)
    return df

df = get_data()

# Header
st.markdown("""
<div style="padding: 1rem 0;">
    <h1 style="color: #000000; font-size: 2.3rem; font-weight: 600;">
        📊 Analisis Data Pendidikan
    </h1>
    <p style="color: #000000; font-size: 1.1rem;">
        Eksplorasi mendalam indikator pendidikan di 27 Kabupaten/Kota Jawa Barat
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Data Mentah", 
    "📈 Tren Pendidikan", 
    "📊 Perbandingan Wilayah",
    "🔬 Analisis Clustering"
])

# ============= TAB 1: DATA MENTAH =============
with tab1:
    st.markdown("### 📋 Data Mentah Pendidikan Jawa Barat")
    
    available_years = sorted(df['tahun'].unique())
    
    # Filter tahun untuk data mentah
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.markdown(f"**Total Data Keseluruhan:** {len(df)} baris")
    with col2:
        selected_year_data = st.selectbox(
            "📅 Pilih Tahun untuk Data Mentah",
            options=["Semua Tahun"] + available_years,
            index=0,
            key="data_year_select"
        )
    with col3:
        n_rows = st.selectbox("Jumlah Baris", [10, 25, 50, 100, 135], index=0, key="rows_select")
    
    # Filter data untuk tabel
    if selected_year_data == "Semua Tahun":
        df_display = df.copy()
    else:
        df_display = df[df['tahun'] == selected_year_data].copy()
    
    # ============================================
    # PAKSA TAHUN TAMPIL TANPA KOMA
    # ============================================
    if 'tahun' in df_display.columns:
        df_display['tahun'] = df_display['tahun'].astype(str)
    
    st.markdown(f"#### 📊 Tabel Data - {selected_year_data}")
    st.dataframe(df_display.head(n_rows), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== STATISTIK DESKRIPTIF DENGAN DROPDOWN ==========
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 📈 Statistik Deskriptif")
    with col2:
        selected_year_stats = st.selectbox(
            "Pilih Tahun",
            options=available_years,
            index=len(available_years)-1,
            key="stats_year_select"
        )
    
    num_cols = ['rls', 'hls', 'amh', 'apm_ma', 'apk', 'persen_penduduk_ma']
    
    col_names = {
        'rls': 'RLS (tahun)',
        'hls': 'HLS (tahun)',
        'amh': 'AMH (%)',
        'apm_ma': 'APM MA (%)',
        'apk': 'APK (%)',
        'persen_penduduk_ma': 'Penduduk Min. SMA (%)'
    }
    
    df_stats = df[df['tahun'] == selected_year_stats][num_cols].describe().round(2)
    
    df_stats.index = [
        'Jumlah Data', 
        'Rata-rata', 
        'Standar Deviasi', 
        'Minimum', 
        'Kuartil 1 (25%)', 
        'Median (50%)', 
        'Kuartil 3 (75%)', 
        'Maksimum'
    ]
    
    df_stats = df_stats.rename(columns=col_names)
    
    st.dataframe(df_stats, use_container_width=True)

# ============= TAB 2: TREN PENDIDIKAN =============
with tab2:    
    # GRAFIK HLS (DENGAN DROPDOWN TOP 5/10/SEMUA)
    st.markdown("#### 🎓 Tren Harapan Lama Sekolah (HLS)")
    
    # 1. Tentukan Top 5 dan Top 10 berdasarkan HLS tahun 2025
    df_2025_hls = df[df['tahun'] == 2025].sort_values('hls', ascending=False)
    top5_hls = df_2025_hls.head(5)['namobj'].tolist()
    top10_hls = df_2025_hls.tail(5)['namobj'].tolist()
    
    # 2. Buat trace/garis untuk SEMUA wilayah
    fig_hls = px.line(
        df,
        x='tahun',
        y='hls',
        color='namobj',
        markers=True,
        title='Tren Harapan Lama Sekolah (HLS) di Jawa Barat',
        labels={'hls': 'Harapan Lama Sekolah (tahun)', 'tahun': 'Tahun', 'namobj': 'Wilayah'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    # 3. Ambil urutan nama wilayah dari grafik
    trace_names_hls = [trace.name for trace in fig_hls.data]
    
    # 4. Buat menu dropdown
    dropdown_buttons_hls = [
        dict(
            label='5 HLS Tertinggi',
            method='update',
            args=[{'visible': [name in top5_hls for name in trace_names_hls]},
                  {'title': 'Tren Harapan Lama Sekolah - Top 5 Wilayah'}]
        ),
        dict(
            label='5 HLS Terendah',
            method='update',
            args=[{'visible': [name in top10_hls for name in trace_names_hls]},
                  {'title': 'Tren Harapan Lama Sekolah - Top 10 Wilayah'}]
        ),
        dict(
            label='Semua Wilayah',
            method='update',
            args=[{'visible': [True] * len(trace_names_hls)},
                  {'title': 'Tren Harapan Lama Sekolah - Semua Wilayah'}]
        )
    ]
    
    # 5. Terapkan dropdown ke layout
    fig_hls.update_layout(
        updatemenus=[dict(
            active=0,
            buttons=dropdown_buttons_hls,
            x=1.15,
            y=1.15,
            xanchor='right',
            yanchor='top'
        )],
        height=450,
        hovermode='x unified',
        legend_title_text='Wilayah',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#000000')
    )
    
    # Setelah fig_hls.update_layout(...)
    fig_hls.update_xaxes(
        tickmode='array',
        tickvals=[2021, 2022, 2023, 2024, 2025],
        ticktext=['2021', '2022', '2023', '2024', '2025'],
        type='category'
    )

    # 6. Set tampilan awal Top 5
    for trace in fig_hls.data:
        trace.visible = trace.name in top5_hls
    
    st.plotly_chart(fig_hls, use_container_width=True)
    
    st.markdown("---")

    # GRAFIK RLS
    st.markdown("#### 📖 Tren Rata-rata Lama Sekolah (RLS)")
    
    df_2025_rls = df[df['tahun'] == 2025].sort_values('rls', ascending=False)
    top5_rls = df_2025_rls.head(5)['namobj'].tolist()
    low5_rls = df_2025_rls.tail(5)['namobj'].tolist()
    
    fig_rls = px.line(
        df, x='tahun', y='rls', color='namobj', markers=True,
        title='Tren Rata-rata Lama Sekolah (RLS) di Jawa Barat',
        labels={'rls': 'RLS (tahun)', 'tahun': 'Tahun', 'namobj': 'Wilayah'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    trace_names_rls = [trace.name for trace in fig_rls.data]
    
    dropdown_buttons_rls = [
        dict(label='5 RLS Tertinggi', method='update',
            args=[{'visible': [name in top5_rls for name in trace_names_rls]},
                  {'title': 'Tren RLS - Top 5 Wilayah Tertinggi'}]),
        dict(label='5 RLS Terendah', method='update',
            args=[{'visible': [name in low5_rls for name in trace_names_rls]},
                  {'title': 'Tren RLS - 5 Wilayah Terendah'}]),
        dict(label='Semua Wilayah', method='update',
            args=[{'visible': [True] * len(trace_names_rls)},
                  {'title': 'Tren RLS - Semua Wilayah'}])
    ]
    
    fig_rls.update_layout(
        updatemenus=[dict(active=0, buttons=dropdown_buttons_rls,
                          x=1.15, y=1.15, xanchor='right', yanchor='top')],
        height=450, hovermode='x unified', legend_title_text='Wilayah',
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#000000')
    )
    
    fig_rls.update_xaxes(
        tickmode='array',
        tickvals=[2021, 2022, 2023, 2024, 2025],
        ticktext=['2021', '2022', '2023', '2024', '2025'],
        type='category'
    )
    
    for trace in fig_rls.data:
        trace.visible = trace.name in top5_rls
    
    st.plotly_chart(fig_rls, use_container_width=True)
    
    # GRAFIK AMH (DENGAN DROPDOWN TOP 5/10/REPRESENTATIF/TERENDAH/SEMUA)
    st.markdown("#### ✍️ Tren Angka Melek Huruf (AMH)")
    
    # 1. Tentukan kategori wilayah berdasarkan AMH tahun 2025
    df_2025_amh = df[df['tahun'] == 2025].sort_values('amh', ascending=False)
    
    top5_amh = df_2025_amh.head(5)['namobj'].tolist()
    low5_amh = df_2025_amh.tail(5)['namobj'].tolist()

    # 2. Buat trace untuk semua wilayah
    fig_amh = px.line(
        df,
        x='tahun',
        y='amh',
        color='namobj',
        markers=True,
        title='Tren Angka Melek Huruf (AMH) di Jawa Barat',
        labels={'amh': 'AMH (%)', 'tahun': 'Tahun', 'namobj': 'Wilayah'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    # 3. Ambil urutan nama wilayah
    trace_names_amh = [trace.name for trace in fig_amh.data]
    
    # 4. Buat menu dropdown
    dropdown_buttons_amh = [
        dict(
            label='5 AMH Tertinggi',
            method='update',
            args=[{'visible': [name in top5_amh for name in trace_names_amh]},
                  {'title': 'Tren Angka Melek Huruf - Top 5 Wilayah Tertinggi'}]
        ),
        dict(
            label='5 AMH Terendah',
            method='update',
            args=[{'visible': [name in low5_amh for name in trace_names_amh]},
                  {'title': 'Tren Angka Melek Huruf - 5 Wilayah Representatif'}]
        ),
        dict(
            label='Semua Wilayah',
            method='update',
            args=[{'visible': [True] * len(trace_names_amh)},
                  {'title': 'Tren Angka Melek Huruf - Semua Wilayah'}]
        )
    ]
    
    # 5. Terapkan dropdown
    fig_amh.update_layout(
        updatemenus=[dict(
            active=0,
            buttons=dropdown_buttons_amh,
            x=1.15,
            y=1.15,
            xanchor='right',
            yanchor='top'
        )],
        height=450,
        hovermode='x unified',
        legend_title_text='Wilayah',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#000000')
    )

    # Setelah fig_amh.update_layout(...)
    fig_amh.update_xaxes(
        tickmode='array',
        tickvals=[2021, 2022, 2023, 2024, 2025],
        ticktext=['2021', '2022', '2023', '2024', '2025'],
        type='category'
    )
    
    # 6. Set tampilan awal Top 5
    for trace in fig_amh.data:
        trace.visible = trace.name in top5_amh
    
    st.plotly_chart(fig_amh, use_container_width=True)

# ============= TAB 3: PERBANDINGAN WILAYAH =============
with tab3:
    st.markdown("### 📊 Perbandingan Persentase Penduduk Minimal SMA 2025")
    
    # Animated bar chart
    df_bar = df.copy()
    
    # Tandai top 5 per tahun
    df_bar['status'] = 0
    for year in df_bar['tahun'].unique():
        top5 = df_bar[df_bar['tahun'] == year].nlargest(5, 'persen_penduduk_ma')['namobj'].tolist()
        df_bar.loc[(df_bar['tahun'] == year) & (df_bar['namobj'].isin(top5)), 'status'] = 1
    
    # Urutan berdasarkan 2025
    y_order = df[df['tahun'] == 2025].sort_values('persen_penduduk_ma', ascending=True)['namobj'].tolist()
    
    fig_bar = px.bar(
        df_bar,
        x='persen_penduduk_ma',
        y='namobj',
        color='status',
        animation_frame='tahun',
        animation_group='namobj',
        orientation='h',
        title='Persentase Penduduk Minimal SMA di Jawa Barat (2021-2025)',
        labels={'persen_penduduk_ma': 'Persentase (%)', 'namobj': 'Kabupaten/Kota'},
        color_discrete_map={0: COLORS['secondary'], 1: COLORS['accent']},
        range_x=[0, df_bar['persen_penduduk_ma'].max() + 5]
    )
    
    fig_bar.update_layout(
        height=700,
        yaxis={'categoryorder': 'array', 'categoryarray': y_order},
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    fig_bar.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1500
    
    st.plotly_chart(fig_bar, use_container_width=True)

# ============= TAB 4: ANALISIS CLUSTERING =============
with tab4:
    st.markdown("### 🔬 Analisis Clustering (K=3)")
    
    with st.spinner("Melakukan clustering..."):
        cluster_results = perform_clustering_all_years(df)
    
    # Scatter plot clustering    
    df_cluster_all = pd.DataFrame()
    for year in range(2021, 2026):
        df_year = df[df['tahun'] == year].copy()
        df_year['cluster_label'] = df_year['namobj'].map(
            cluster_results.drop('Silhouette Score', errors='ignore')[f'cluster_{year}']
        )
        df_cluster_all = pd.concat([df_cluster_all, df_year], ignore_index=True)
    
    fig_scatter = px.scatter(
        df_cluster_all,
        x='rls',
        y='persen_penduduk_ma',
        color='cluster_label',
        animation_frame='tahun',
        animation_group='namobj',
        text='namobj',
        hover_name='namobj',
        color_discrete_map=CLUSTER_COLORS,
        title='Segmentasi Kab/Kota Jawa Barat (2021-2025)',
        labels={'rls': 'RLS (tahun)', 'persen_penduduk_ma': 'Penduduk Min. SMA (%)'}
    )
    
    fig_scatter.update_traces(
        textposition='top center',
        marker=dict(size=12, line=dict(width=1, color='white')),
        textfont=dict(size=9)
    )
    
    fig_scatter.update_layout(
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    fig_scatter.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1500
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Stacked bar chart
    st.markdown("#### 📈 Perkembangan Jumlah Wilayah per Cluster")
    
    cluster_summary = get_cluster_summary(cluster_results)
    
    fig_stack = px.bar(
        cluster_summary,
        x='tahun',
        y='jumlah_wilayah',
        color='cluster',
        text='jumlah_wilayah',
        title='Perkembangan Jumlah Kabupaten/Kota per Cluster (2021-2025)',
        color_discrete_map=CLUSTER_COLORS,
        category_orders={'cluster': ['Rendah', 'Sedang', 'Tinggi']}
    )
    
    fig_stack.update_layout(
        barmode='stack',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    fig_stack.update_traces(textfont_size=14, textposition="inside")
    
    st.plotly_chart(fig_stack, use_container_width=True)