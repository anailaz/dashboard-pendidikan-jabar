"""
Halaman About
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
        ℹ️ Tentang Kami
    </h1>
    <p style="color: #000000; font-size: 1.1rem;">
        Official Statistics Dashboard Project - Kelompok 6
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# DESKRIPSI PROJECT
# ============================================
st.markdown(f"""
<div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.8rem; 
            margin-bottom: 2rem; border-left: 4px solid {COLORS['primary']};">
    <h3 style="color: #000000; margin-bottom: 1rem;">📊 Tentang Project Ini</h3>
    <p style="color: #000000; line-height: 1.8; font-size: 1.05rem;">
        Dashboard <strong>Official Statistics</strong> ini dikembangkan sebagai bagian dari 
        tugas mata kuliah Official Statistics. Project ini bertujuan untuk menyajikan 
        analisis struktur pendidikan penduduk usia produktif di Provinsi Jawa Barat 
        secara interaktif, informatif, dan mudah dipahami.
    </p>
    <p style="color: #000000; line-height: 1.8; font-size: 1.05rem; margin-top: 1rem;">
        Melalui dashboard ini, kami berharap dapat memberikan gambaran yang jelas mengenai 
        kondisi pendidikan di 27 Kabupaten/Kota di Jawa Barat selama periode 2021-2025, 
        serta menjadi referensi bagi pengambil kebijakan, akademisi, dan masyarakat umum 
        dalam memahami dinamika pendidikan di wilayah tersebut.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# TUJUAN & MANFAAT
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.5rem; 
                height: 100%;">
        <h3 style="color: #000000; margin-bottom: 1rem;">🎯 Tujuan</h3>
        <ul style="color: #000000; line-height: 2; padding-left: 1.2rem;">
            <li>Mengidentifikasi pola distribusi tingkat pendidikan di Jawa Barat</li>
            <li>Melihat ketimpangan pendidikan antar wilayah kabupaten/kota</li>
            <li>Menyediakan visualisasi data yang interaktif dan mudah dipahami</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.5rem; 
                height: 100%;">
        <h3 style="color: #000000; margin-bottom: 1rem;">💡 Manfaat</h3>
        <ul style="color: #000000; line-height: 2; padding-left: 1.2rem;">
            <li>Membantu identifikasi wilayah prioritas untuk intervensi kebijakan</li>
            <li>Menyediakan insight berbasis data untuk pengambilan keputusan</li>
            <li>Menjadi referensi akademik untuk penelitian selanjutnya</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# SUMBER DATA
# ============================================
st.markdown(f"""
<div style="background: {COLORS['secondary']}; border-radius: 12px; padding: 1.5rem; 
            margin-bottom: 2rem;">
    <h3 style="color: #000000; margin-bottom: 0.8rem;">📚 Sumber Data</h3>
    <p style="color: #000000; line-height: 1.8; font-size: 1.05rem;">
        Data yang digunakan dalam dashboard ini bersumber dari 
        <strong>Badan Pusat Statistik (BPS) Provinsi Jawa Barat</strong> 
        untuk periode tahun 2021-2025, mencakup 6 indikator utama pendidikan:
    </p>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
        <span style="background: {COLORS['primary']}; color: #000000; padding: 0.3rem 1rem; 
                     border-radius: 20px; font-size: 0.9rem;">Rata-rata Lama Sekolah (RLS)</span>
        <span style="background: {COLORS['primary']}; color: #000000; padding: 0.3rem 1rem; 
                     border-radius: 20px; font-size: 0.9rem;">Harapan Lama Sekolah (HLS)</span>
        <span style="background: {COLORS['primary']}; color: #000000; padding: 0.3rem 1rem; 
                     border-radius: 20px; font-size: 0.9rem;">Angka Melek Huruf (AMH)</span>
        <span style="background: {COLORS['primary']}; color: #000000; padding: 0.3rem 1rem; 
                     border-radius: 20px; font-size: 0.9rem;">Angka Partisipasi Murni SMA Sederajat</span>
        <span style="background: {COLORS['primary']}; color: #000000; padding: 0.3rem 1rem; 
                     border-radius: 20px; font-size: 0.9rem;">Angka Partisipasi Kasar</span>
        <span style="background: {COLORS['primary']}; color: #000000; padding: 0.3rem 1rem; 
                     border-radius: 20px; font-size: 0.9rem;">% Penduduk Minimal SMA</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# ANGGOTA TIM
# ============================================
st.markdown("<h3 style='color: #000000; margin-bottom: 1.5rem;'>👥 Anggota Tim</h3>", unsafe_allow_html=True)

team = [
    {"name": "Octaviani Putri Al Fajri", "nim": "164221042", "role": "📝 Laporan", "icon": "📄"},
    {"name": "Sabrina Indy Safira", "nim": "164221072", "role": "📊 Analisis Data", "icon": "📈"},
    {"name": "Jovita Suryo Angeline", "nim": "164221094", "role": "📝 Laporan", "icon": "📄"},
    {"name": "Amira Naila Zanira", "nim": "164221100", "role": "🎨 Analisis Data & Dashboard", "icon": "💻"},
    {"name": "Kania Putri Octavia", "nim": "164231111", "role": "📥 Pengumpulan Data & Laporan", "icon": "📋"},
]

cols = st.columns(len(team))
for i, member in enumerate(team):
    with cols[i]:
        st.markdown(f"""
        <div style="background: {COLORS['background']}; border-radius: 12px; padding: 1.2rem 0.8rem; 
                    box-shadow: 0 2px 10px rgba(0,0,0,0.05); text-align: center;
                    border-top: 4px solid {COLORS['accent']}; height: 100%;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{member['icon']}</div>
            <h4 style="color: #000000; margin: 0.5rem 0; font-size: 1rem; font-weight: 600;">{member['name']}</h4>
            <p style="color: #000000; font-size: 0.85rem; margin-bottom: 0.3rem;">{member['nim']}</p>
            <p style="color: {COLORS['accent']}; font-weight: 500; font-size: 0.85rem; margin: 0;">{member['role']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# TOOLS & TEKNOLOGI
# ============================================
st.markdown("<h3 style='color: #000000; margin-bottom: 1rem;'>🛠️ Tools & Teknologi</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 10px; padding: 1rem; 
                text-align: center; height: 100%;">
        <span style="font-size: 2.5rem;">🐍</span>
        <h5 style="color: #000000; margin: 0.5rem 0;">Python</h5>
        <p style="color: #000000; font-size: 0.85rem;">Pandas, NumPy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 10px; padding: 1rem; 
                text-align: center; height: 100%;">
        <span style="font-size: 2.5rem;">📊</span>
        <h5 style="color: #000000; margin: 0.5rem 0;">Streamlit</h5>
        <p style="color: #000000; font-size: 0.85rem;">Web Framework</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 10px; padding: 1rem; 
                text-align: center; height: 100%;">
        <span style="font-size: 2.5rem;">📈</span>
        <h5 style="color: #000000; margin: 0.5rem 0;">Plotly</h5>
        <p style="color: #000000; font-size: 0.85rem;">Visualisasi Interaktif</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="background: {COLORS['background']}; border-radius: 10px; padding: 1rem; 
                text-align: center; height: 100%;">
        <span style="font-size: 2.5rem;">🔬</span>
        <h5 style="color: #000000; margin: 0.5rem 0;">Scikit-learn</h5>
        <p style="color: #000000; font-size: 0.85rem;">K-Means Clustering</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# KONTAK / INFORMASI TAMBAHAN
st.markdown(f"""
<div style="background: {COLORS['primary']}20; border-radius: 12px; padding: 1.5rem; 
            text-align: center; margin-top: 1rem;">
    <p style="color: #000000; margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;">
        © 2026 Official Statistics Dashboard - Kelompok 6. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)