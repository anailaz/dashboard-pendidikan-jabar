"""
Official Statistics Dashboard - Pendidikan Jawa Barat
Entry point aplikasi Streamlit
"""

import streamlit as st

# Konfigurasi halaman - HARUS menjadi perintah Streamlit pertama
st.set_page_config(
    page_title="Dashboard Pendidikan Jabar",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS kustom dengan palette baru dan font hitam
st.markdown("""
<style>
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #7DAACB 0%, #5B8FB5 100%);
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] h2 {
        color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] p {
        color: #000000 !important;
    }
    
    /* Sidebar info box */
    .sidebar-info {
        background: rgba(255, 253, 235, 0.5) !important;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .sidebar-info p {
        color: #000000 !important;
    }
    
    .sidebar-info strong {
        color: #000000 !important;
    }
    
    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom classes */
    .sidebar-header {
        text-align: center;
        padding: 1.5rem 0.5rem;
    }
    
    .sidebar-footer {
        margin-top: 2rem;
        opacity: 0.9;
        text-align: center;
    }
    
    /* Main content text */
    h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #000000 !important;
    }
    
    /* Links */
    a {
        color: #CE2626 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #7DAACB !important;
        color: #000000 !important;
        border: none !important;
    }
    
    .stButton > button:hover {
        background-color: #E8DBB3 !important;
        color: #000000 !important;
    }
    
    /* Tabs */
    .stTabs [aria-selected="true"] {
        border-bottom-color: #CE2626 !important;
    }
    
    /* Welcome container */
    .welcome-container {
        text-align: center;
        padding: 3rem 1rem;
        background: #FFFDEB;
        border-radius: 20px;
        margin: 2rem 0;
    }
    
    .welcome-container h1 {
        color: #000000;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .welcome-container p {
        color: #000000;
        font-size: 1.2rem;
    }
    
    .nav-hint {
        text-align: center;
        padding: 1.5rem;
        background: #E8DBB3;
        border-radius: 10px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def render_sidebar():
    """
    Fungsi untuk merender sidebar yang KONSISTEN di semua halaman
    """
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <h2>📚 Official Statistics</h2>
            <p style="font-size: 0.9rem;">Pendidikan Jawa Barat</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div class="sidebar-info">
            <p><strong>📅 Periode:</strong> 2021-2025</p>
            <p><strong>📍 Wilayah:</strong> 27 Kab/Kota</p>
            <p><strong>📊 Indikator:</strong> 6 Variabel</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div class="sidebar-footer">
            <p style="font-size: 0.8rem;">
                Kelompok 6 - Official Statistics<br>
                © 2026
            </p>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Fungsi utama - halaman welcome"""
    
    # Render sidebar yang konsisten
    render_sidebar()
    
    # Halaman utama - welcome message
    st.markdown("""
    <div class="welcome-container">
        <h1>📊 Selamat Datang di Dashboard</h1>
        <h2 style="color: #000000; font-size: 1.5rem; margin-bottom: 2rem;">
            Official Statistics Pendidikan Jawa Barat
        </h2>
        <div style="width: 100px; height: 3px; background: #CE2626; margin: 0 auto 2rem;"></div>
        <p style="font-size: 1.2rem; color: #000000;">
            👈 Silakan pilih halaman dari sidebar untuk memulai
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="nav-hint">
        <p style="color: #000000; margin: 0;">
            Halaman yang tersedia:<br>
            <strong style="font-size: 1.1rem;">🏠 Beranda</strong> &nbsp;|&nbsp;
            <strong style="font-size: 1.1rem;">📊 Analisis</strong> &nbsp;|&nbsp;
            <strong style="font-size: 1.1rem;">💡 Insight</strong> &nbsp;|&nbsp;
            <strong style="font-size: 1.1rem;">ℹ️ About</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()