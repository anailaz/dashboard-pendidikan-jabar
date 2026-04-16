"""
Halaman Beranda
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from utils.data_loader import load_raw_data, preprocess_data
from config.settings import COLORS

# Import fungsi sidebar dari app.py
from app import render_sidebar

# Render sidebar yang konsisten
render_sidebar()

# Load data
@st.cache_data
def get_data():
    df_raw = load_raw_data()
    df = preprocess_data(df_raw)
    return df

# Header
st.markdown(f"""
<div style="text-align: center; padding: 1rem 0;">
    <h1 style="color: #000000; font-size: 2.3rem; font-weight: 700; margin-bottom: 0.3rem;">
        Analisis Struktur Pendidikan
    </h1>
    <p style="color: #000000; font-size: 1.2rem;">
        Penduduk Usia Produktif di Jawa Barat
    </p>
    <div style="width: 80px; height: 3px; background: {COLORS['accent']}; margin: 0.5rem auto;"></div>
</div>
""", unsafe_allow_html=True)

# Load data
try:
    df = get_data()
    df_2025 = df[df['tahun'] == 2025]
    data_loaded = True
except Exception as e:
    data_loaded = False
    st.error(f"Error loading data: {e}")

# Layout Latar Belakang
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; 
                border-radius: 12px; 
                padding: 1.5rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05);
                height: 100%;">
        <h3 style="color: #000000; margin-bottom: 1rem; margin-top: 0;">📖 Latar Belakang</h3>
        <p style="line-height: 1.7; color: #000000; margin-bottom: 0.8rem; font-size: 0.95rem;">
            Pendidikan memiliki peran penting dalam meningkatkan kualitas sumber daya manusia, 
            khususnya pada penduduk usia produktif yang menjadi penggerak utama pembangunan ekonomi 
            dan sosial. Di <strong>Jawa Barat</strong>, perkembangan pendidikan menunjukkan tren positif, yang tercermin 
            dari meningkatnya partisipasi sekolah serta perluasan akses terhadap pendidikan formal.  
            Oleh karena itu, pemantauan kondisi pendidikan perlu dilakukan secara sistematis agar kebijakan 
            yang diambil dapat lebih tepat sasaran.
        </p>
        <p style="line-height: 1.7; color: #000000; margin-top: 0.8rem; font-size: 0.95rem;">
            Namun, penyajian data dalam bentuk statis memberikan batasan dalam proses analisis. 
            Oleh karena itu, kami mengembangkan dashboard interaktif untuk mengatasi hal tersebut
            dengan menyajikan data secara visual, dinamis, dan mudah dipahami. Melalui fitur seperti filter, 
            visualisasi tren, dan eksplorasi data, dashboard ini kami harap dapat membantu pengguna 
            dalam mengeksplorasi data serta mendukung pengambilan keputusan berbasis data secara lebih efektif.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if data_loaded:
        total_wilayah = df['namobj'].nunique()
        total_tahun = df['tahun'].nunique()
    else:
        total_wilayah = 27
        total_tahun = 5
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {COLORS['background']} 0%, {COLORS['secondary']} 100%); 
                border-radius: 15px; 
                padding: 1.2rem 1rem; 
                border-left: 4px solid {COLORS['accent']};
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;">
        <h3 style="color: #000000; margin-bottom: 1.2rem; text-align: center; margin-top: 0; font-size: 1.3rem;">
            📊 Cakupan Data
        </h3>
        <div style="text-align: center;">
            <div style="margin-bottom: 1rem;">
                <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0 0 0.2rem 0;">
                    {total_wilayah}
                </p>
                <p style="color: #000000; font-size: 0.85rem; margin: 0;">Kabupaten/Kota</p>
            </div>
            <div style="margin-bottom: 1rem;">
                <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0 0 0.2rem 0;">
                    {total_tahun}
                </p>
                <p style="color: #000000; font-size: 0.85rem; margin: 0;">Tahun (2021-2025)</p>
            </div>
            <div>
                <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0 0 0.2rem 0;">
                    6
                </p>
                <p style="color: #000000; font-size: 0.85rem; margin: 0;">Indikator Pendidikan</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Key Metrics
st.markdown("""
<div style="margin: 1.5rem 0;">
    <h3 style="color: #000000;">📈 Key Metrics</h3>
    <p style="color: #000000;">Indikator Utama Pendidikan Jawa Barat 2025</p>
</div>
""", unsafe_allow_html=True)

if data_loaded:
    avg_rls = df_2025['rls'].mean()
    avg_hls = df_2025['hls'].mean()
    avg_persen = df_2025['persen_penduduk_ma'].mean()
    avg_amh = df_2025['amh'].mean()
    top_region = df_2025.nlargest(1, 'rls')['namobj'].values[0]
    bottom_region = df_2025.nsmallest(1, 'rls')['namobj'].values[0]
else:
    avg_rls = 9.33
    avg_hls = 13.15
    avg_persen = 29.77
    avg_amh = 99.02
    top_region = "Kota Bekasi"
    bottom_region = "Indramayu"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.2rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid {COLORS['primary']};">
        <p style="color: #000000; font-size: 0.85rem; margin: 0;">📖 Rata-rata Lama Sekolah</p>
        <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0.3rem 0;">{avg_rls:.2f}</p>
        <p style="color: #000000; font-size: 0.9rem; margin: 0;">tahun</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.2rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid {COLORS['secondary']};">
        <p style="color: #000000; font-size: 0.85rem; margin: 0;">🎓 Harapan Lama Sekolah</p>
        <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0.3rem 0;">{avg_hls:.2f}</p>
        <p style="color: #000000; font-size: 0.9rem; margin: 0;">tahun</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.2rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid {COLORS['accent']};">
        <p style="color: #000000; font-size: 0.85rem; margin: 0;">📊 Penduduk Min. SMA</p>
        <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0.3rem 0;">{avg_persen:.2f}</p>
        <p style="color: #000000; font-size: 0.9rem; margin: 0;">persen</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.2rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid {COLORS['primary']};">
        <p style="color: #000000; font-size: 0.85rem; margin: 0;">✍️ Angka Melek Huruf</p>
        <p style="font-size: 2rem; font-weight: 700; color: #000000; margin: 0.3rem 0;">{avg_amh:.2f}</p>
        <p style="color: #000000; font-size: 0.9rem; margin: 0;">persen</p>
    </div>
    """, unsafe_allow_html=True)

# Wilayah info
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.5rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <h4 style="color: #000000;">🏆 Wilayah dengan Pendidikan Tertinggi</h4>
        <p style="font-size: 1.3rem; margin: 0.5rem 0; color: #000000;"><strong>{top_region}</strong></p>
        <p style="color: #000000;">Memimpin dalam indikator pendidikan</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.5rem; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <h4 style="color: #000000;">⚠️ Wilayah dengan Pendidikan Terendah</h4>
        <p style="font-size: 1.3rem; margin: 0.5rem 0; color: #000000;"><strong>{bottom_region}</strong></p>
        <p style="color: #000000;">Membutuhkan perhatian khusus</p>
    </div>
    """, unsafe_allow_html=True)

# Insight Utama
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #000000;'>💡 Insight Utama</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['secondary']}; border-radius: 12px; padding: 1.5rem; 
                border: 1px solid {COLORS['accent']}; height: 100%;">
        <h4 style="color: #000000;"> Insight 1: Tren Positif tapi Tidak Merata</h4>
        <p style="color: #000000; line-height: 1.6;">
            Tren pendidikan di Jawa Barat menunjukkan peningkatan yang konsisten selama periode 2021–2025, terutama pada indikator 
            Harapan Lama Sekolah (HLS) dan Rata-rata Lama Sekolah (RLS). Hal ini mencerminkan adanya perbaikan dalam akses dan partisipasi 
            pendidikan. Namun, laju peningkatan tidak merata di seluruh wilayah, di mana beberapa daerah seperti Kota Bekasi mengalami 
            pertumbuhan yang lebih stabil, sementara wilayah lain seperti Kota Bogor dan Cimahi menunjukkan fluktuasi. 
            Kondisi ini mengindikasikan bahwa peningkatan kualitas pendidikan masih belum berlangsung secara konsisten di semua daerah.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['secondary']}; border-radius: 12px; padding: 1.5rem; 
                border: 1px solid {COLORS['accent']}; height: 100%;">
        <h4 style="color: #000000;">Insight 2: Ketimpangan Wilayah Masih Tinggi</h4>
        <p style="color: #000000; line-height: 1.6;">
            Ketimpangan pendidikan antar wilayah di Jawa Barat masih sangat signifikan. Wilayah perkotaan seperti Kota Bekasi dan Depok 
            secara konsisten menunjukkan capaian pendidikan yang tinggi, ditandai dengan RLS di atas 11 tahun dan persentase penduduk 
            minimal SMA yang melebihi 40%. Sebaliknya, wilayah kabupaten seperti Cianjur dan Tasikmalaya masih tertinggal dengan RLS 
            sekitar 7–8 tahun dan persentase pendidikan minimal SMA di bawah 25%. Meskipun terjadi peningkatan dari tahun ke tahun, 
            kesenjangan antar wilayah ini tetap lebar dan menunjukkan bahwa pemerataan akses serta kualitas pendidikan masih menjadi tantangan utama.
        </p>
    </div>
    """, unsafe_allow_html=True)