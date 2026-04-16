"""
Komponen reusable untuk metrics dan cards
"""

import streamlit as st
from config.settings import COLORS

def metric_card(title, value, suffix="", prefix="", icon="📊", color=COLORS['primary']):
    """
    Menampilkan metric card yang stylish
    
    Args:
        title (str): Judul metric
        value: Nilai metric
        suffix (str): Suffix untuk nilai
        prefix (str): Prefix untuk nilai
        icon (str): Emoji icon
        color (str): Warna border
    """
    html = f"""
    <div class="metric-card" style="border-left-color: {color};">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 1.5rem; margin-right: 0.5rem;">{icon}</span>
            <span class="metric-label">{title}</span>
        </div>
        <div class="metric-value">
            {prefix}{value:,.2f}{suffix}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def insight_callout(title, content, icon="💡"):
    """
    Menampilkan insight callout box
    
    Args:
        title (str): Judul insight
        content (str): Konten insight
        icon (str): Emoji icon
    """
    html = f"""
    <div class="insight-callout">
        <h4>{icon} {title}</h4>
        <p>{content}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def section_header(title, description=None):
    """
    Menampilkan section header
    
    Args:
        title (str): Judul section
        description (str): Deskripsi section (opsional)
    """
    html = f"""
    <div class="section-header">
        <h2>{title}</h2>
        {f'<p>{description}</p>' if description else ''}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def filter_section(df):
    """
    Menampilkan filter section
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        
    Returns:
        tuple: (selected_years, selected_regions)
    """
    from utils.data_loader import get_unique_years, get_unique_regions
    
    st.markdown('<div class="filter-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        years = get_unique_years(df)
        selected_years = st.multiselect(
            "📅 Pilih Tahun",
            options=years,
            default=years
        )
    
    with col2:
        regions = get_unique_regions(df)
        selected_regions = st.multiselect(
            "📍 Pilih Wilayah",
            options=regions,
            default=[]
        )
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Reset Filter", use_container_width=True):
            selected_years = years
            selected_regions = []
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return selected_years, selected_regions