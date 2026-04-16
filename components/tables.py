"""
Komponen reusable untuk tabel
"""

import streamlit as st
import pandas as pd
from config.settings import COLORS

def display_dataframe(df, height=400, use_container_width=True):
    """
    Menampilkan DataFrame dengan styling
    
    Args:
        df (pd.DataFrame): DataFrame yang akan ditampilkan
        height (int): Tinggi tabel
        use_container_width (bool): Gunakan lebar container penuh
    """
    st.dataframe(
        df,
        height=height,
        use_container_width=use_container_width,
        hide_index=False
    )

def display_cluster_table(cluster_results, show_silhouette=False):
    """
    Menampilkan tabel hasil clustering
    
    Args:
        cluster_results (pd.DataFrame): Hasil clustering
        show_silhouette (bool): Tampilkan silhouette score
    """
    df_display = cluster_results.copy()
    
    if not show_silhouette:
        df_display = df_display.drop('Silhouette Score', errors='ignore')
    
    # Styling untuk cluster
    def highlight_cluster(val):
        if val == 'Rendah':
            return f'background-color: {COLORS["accent"]}; color: #2C3E50'
        elif val == 'Sedang':
            return f'background-color: {COLORS["secondary"]}; color: white'
        elif val == 'Tinggi':
            return f'background-color: {COLORS["primary"]}; color: white'
        return ''
    
    # Terapkan styling
    styled_df = df_display.style.applymap(
        highlight_cluster,
        subset=[col for col in df_display.columns if col.startswith('cluster_')]
    )
    
    st.dataframe(
        styled_df,
        height=500,
        use_container_width=True
    )

def display_change_table(changes_df):
    """
    Menampilkan tabel perubahan cluster
    
    Args:
        changes_df (pd.DataFrame): DataFrame perubahan cluster
    """
    # Filter hanya yang berubah
    changes_filtered = changes_df[changes_df['cluster_2021'] != changes_df['cluster_2025']]
    
    if not changes_filtered.empty:
        st.markdown("#### 📈 Wilayah dengan Perubahan Cluster (2021 → 2025)")
        
        display_cols = ['cluster_2021', 'cluster_2025', 'Perubahan_2021_2025']
        
        # Styling
        def highlight_change(val):
            if '→' in str(val):
                if 'Rendah → Sedang' in val or 'Sedang → Tinggi' in val:
                    return 'background-color: #D4EDDA; color: #155724'
                elif 'Sedang → Rendah' in val or 'Tinggi → Sedang' in val:
                    return 'background-color: #F8D7DA; color: #721C24'
            return ''
        
        styled_df = changes_filtered[display_cols].style.applymap(
            highlight_change,
            subset=['Perubahan_2021_2025']
        )
        
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.info("Tidak ada perubahan cluster yang signifikan.")

def display_pagination_table(df, page_size=10, key_prefix="table"):
    """
    Menampilkan tabel dengan pagination
    
    Args:
        df (pd.DataFrame): DataFrame yang akan ditampilkan
        page_size (int): Jumlah baris per halaman
        key_prefix (str): Prefix untuk session state key
    """
    total_rows = len(df)
    total_pages = (total_rows - 1) // page_size + 1
    
    if f"{key_prefix}_page" not in st.session_state:
        st.session_state[f"{key_prefix}_page"] = 1
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("◀ Previous", key=f"{key_prefix}_prev"):
            if st.session_state[f"{key_prefix}_page"] > 1:
                st.session_state[f"{key_prefix}_page"] -= 1
    
    with col2:
        st.markdown(f"<p style='text-align: center;'>Page {st.session_state[f'{key_prefix}_page']} of {total_pages}</p>", 
                   unsafe_allow_html=True)
    
    with col3:
        if st.button("Next ▶", key=f"{key_prefix}_next"):
            if st.session_state[f"{key_prefix}_page"] < total_pages:
                st.session_state[f"{key_prefix}_page"] += 1
    
    # Hitung indeks
    start_idx = (st.session_state[f"{key_prefix}_page"] - 1) * page_size
    end_idx = min(start_idx + page_size, total_rows)
    
    # Tampilkan data
    st.dataframe(df.iloc[start_idx:end_idx], use_container_width=True)
    
    st.caption(f"Showing {start_idx + 1}-{end_idx} of {total_rows} rows")