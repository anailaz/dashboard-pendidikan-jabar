"""
Halaman Insight
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from config.settings import COLORS

# Import fungsi sidebar dari app.py
from app import render_sidebar

# Render sidebar yang konsisten
render_sidebar()

# Header
st.markdown(f"""
<div style="padding: 1rem 0;">
    <h1 style="color: #000000; font-size: 2.3rem; font-weight: 600;">
        💡 Insight & Interpretasi
    </h1>
    <p style="color: #000000; font-size: 1.1rem;">
        Temuan kunci dan rekomendasi kebijakan berdasarkan analisis data pendidikan Jawa Barat (2021-2025)
    </p>
</div>
""", unsafe_allow_html=True)

# RINGKASAN SINGKAT
st.markdown("### 📊 Ringkasan Singkat")

st.markdown(f"""
<div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
            margin-bottom: 2rem; border-left: 4px solid {COLORS['primary']};">
    <p style="color: #000000; line-height: 1.9; font-size: 1.05rem;">
        Secara umum, indikator pendidikan di Jawa Barat menunjukkan tren positif selama periode 2021-2025. 
        <strong>Rata-rata Lama Sekolah (RLS)</strong> meningkat dari 9,04 menjadi 9,33 tahun, 
        <strong>Harapan Lama Sekolah (HLS)</strong> mencapai 13,15 tahun, dan 
        <strong>Angka Melek Huruf (AMH)</strong> sudah mendekati universal di angka 99,02%. 
        Namun, <strong>persentase penduduk minimal SMA</strong> masih rendah yaitu sekitar 29,77% dan 
        <strong>kesenjangan antar wilayah</strong> masih menjadi tantangan utama yang perlu segera diatasi.
    </p>
</div>
""", unsafe_allow_html=True)

# INSIGHT 1: TREN RLS DAN HLS
st.markdown("### 📈 Tren Peningkatan Indikator Utama")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
                border-left: 4px solid {COLORS['primary']}; height: 100%;">
        <h4 style="color: #000000; margin-bottom: 1rem;">📖 Rata-rata Lama Sekolah (RLS)</h4>
        <p style="color: #000000; line-height: 1.8;">
            RLS Jawa Barat meningkat dari 9,04 tahun (2021) menjadi 9,33 tahun (2025), 
            atau naik sebesar 0,29 tahun dalam lima tahun. Angka ini setara dengan tambahan 
            pendidikan sekitar 3,5 bulan. Meskipun menunjukkan perbaikan, laju pertumbuhan rata-rata 
            hanya 0,058 per tahun, masih tergolong lambat untuk mencapai target wajib belajar 12 tahun.
        </p>
        <p style="color: #000000; line-height: 1.8; margin-top: 1rem;">
            Wilayah dengan RLS tertinggi adalah Kota Bekasi (12,07 tahun), diikuti Kota Depok (11,78 tahun) 
            dan Kota Bandung (11,37 tahun). Sementara wilayah dengan RLS terendah adalah Indramayu (7,67 tahun), 
            Tasikmalaya (8,15 tahun), dan Cianjur (8,17 tahun).
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
                border-left: 4px solid {COLORS['secondary']}; height: 100%;">
        <h4 style="color: #000000; margin-bottom: 1rem;">🎓 Harapan Lama Sekolah (HLS)</h4>
        <p style="color: #000000; line-height: 1.8;">
            HLS rata-rata Jawa Barat mencapai 13,15 tahun pada 2025, menunjukkan bahwa 
            anak-anak di provinsi ini memiliki harapan untuk menempuh pendidikan hingga jenjang 
            diploma (D1/D2). Angka ini sudah melampaui target wajib belajar 12 tahun.
        </p>
        <p style="color: #000000; line-height: 1.8; margin-top: 1rem;">
            Wilayah dengan HLS tertinggi adalah Ciamis (14,50 tahun), diikuti Kota Bandung (14,38 tahun) 
            dan Kota Depok (14,28 tahun). Sementara HLS terendah terdapat di Bandung Barat (12,26 tahun) 
            dan Karawang (12,29 tahun). Selisih antara HLS tertinggi dan terendah mencapai 2,25 tahun, 
            menunjukkan adanya disparitas harapan pendidikan antar wilayah.
        </p>
    </div>
    """, unsafe_allow_html=True)

# INSIGHT 2: AMH DAN PERSENTASE PENDUDUK MINIMAL SMA
st.markdown("### 📚 Indikator Literasi dan Jenjang Pendidikan")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
                border-left: 4px solid #27ae60; height: 100%;">
        <h4 style="color: #000000; margin-bottom: 1rem;">✍️ Angka Melek Huruf (AMH)</h4>
        <p style="color: #000000; line-height: 1.8;">
            AMH Jawa Barat mencapai 99,02% pada tahun 2025, menunjukkan bahwa 
            hampir seluruh penduduk usia 15 tahun ke atas sudah mampu membaca dan menulis. 
            Ini merupakan capaian yang sangat baik dan mendekati universal.
        </p>
        <p style="color: #000000; line-height: 1.8; margin-top: 1rem;">
            Kota Sukabumi berhasil mencapai AMH 100%, menjadi satu-satunya wilayah dengan tingkat melek 
            huruf sempurna. Wilayah dengan AMH terendah adalah Cirebon (95,48%), namun angka ini masih 
            tergolong tinggi. Peningkatan tercepat terjadi di Indramayu yang naik dari 93,76% (2021) 
            menjadi 98,20% (2025) atau meningkat 4,44 poin persentase.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
                border-left: 4px solid {COLORS['accent']}; height: 100%;">
        <h4 style="color: #000000; margin-bottom: 1rem;">📊 Persentase Penduduk Minimal SMA</h4>
        <p style="color: #000000; line-height: 1.8;">
            Rata-rata persentase penduduk usia 25 tahun ke atas yang berpendidikan minimal SMA di Jawa Barat 
            baru mencapai 29,77% pada tahun 2025. Artinya, hanya 1 dari 3 penduduk dewasa yang telah menamatkan pendidikan menengah.
        </p>
        <p style="color: #000000; line-height: 1.8; margin-top: 1rem;">
            Kesenjangan pada indikator ini sangat ekstrem. Wilayah tertinggi adalah Bekasi (49,24%) dan terendah Tasikmalaya (15,84%), 
            dengan selisih mencapai 33,40 poin persentase. Kondisi ini menunjukkan bahwa akses 
            dan keberlanjutan pendidikan ke jenjang menengah masih menjadi pekerjaan rumah besar bagi sebagian besar kabupaten di Jawa Barat.
        </p>
    </div>
    """, unsafe_allow_html=True)

# INSIGHT 3: KETIMPANGAN WILAYAH
st.markdown("### 📍 Ketimpangan Wilayah")

st.markdown(f"""
<div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
            margin-bottom: 1.5rem; border-left: 4px solid #e74c3c;">
    <p style="color: #000000; line-height: 1.9; font-size: 1.05rem;">
        Analisis data menunjukkan adanya kesenjangan antara wilayah perkotaan dan kabupaten di Jawa Barat. 
        Rasio ketimpangan RLS mencapai 1,57 kali antara wilayah tertinggi Kota Bekasi dan wilayah terendah Kabupaten Indramayu, dengan selisih absolut sebesar 
        4,40 tahun pendidikan (setara dengan tidak tamat SD hingga hampir tamat SMP).
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# INSIGHT 4: INTERPRETASI HASIL CLUSTERING
# ============================================================================
st.markdown("### 🔬 Interpretasi Hasil Clustering")

st.markdown(f"""
<div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
            margin-bottom: 1.5rem; border-left: 4px solid #9b59b6;">
    <p style="color: #000000; line-height: 1.9; font-size: 1.05rem;">
        Hasil clustering K-Means (K=3) menunjukkan polarisasi tajam antara kota dan kabupaten. 
        Cluster <strong>Tinggi</strong> (6 wilayah) didominasi kota besar seperti Bekasi, Depok, Bandung, dan Cimahi. 
        Cluster <strong>Sedang</strong> (13 wilayah) mencakup campuran kota kecil dan kabupaten berkembang seperti Bogor, Bandung, Karawang, dan Sumedang. 
        Sementara cluster <strong>Rendah</strong> (8 wilayah) seluruhnya kabupaten, dengan Indramayu, Cirebon, dan Subang yang konsisten tertinggal sepanjang 2021-2025.
    </p>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown(f"""
<div style="text-align: center; padding: 1.5rem; margin-top: 1rem; 
            border-top: 1px solid #e0e0e0;">
    <p style="color: #666; font-size: 0.85rem;">
        📊 Sumber: Analisis Data BPS Jawa Barat (2021-2025) | Indikator: RLS, HLS, AMH, Persentase Penduduk Minimal SMA<br>
        © 2026 Official Statistics Dashboard - Kelompok 6
    </p>
</div>
""", unsafe_allow_html=True)