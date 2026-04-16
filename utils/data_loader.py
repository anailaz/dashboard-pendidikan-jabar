"""
Data loader untuk membaca dan memproses data
"""

import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data
def load_raw_data():
    """Load data dari file CSV"""
    
    # CARI FILE CSV
    csv_path = None
    possible_paths = [
        Path(__file__).parent.parent / "UTS OS KEL 6 - variabel.csv",
        Path(__file__).parent.parent.parent / "UTS OS KEL 6 - variabel.csv",
        Path.cwd() / "UTS OS KEL 6 - variabel.csv",
        Path.cwd() / "data" / "UTS OS KEL 6 - variabel.csv",
    ]
    
    for path in possible_paths:
        if path.exists():
            csv_path = path
            break
    
    if csv_path is None:
        for file in Path.cwd().glob("*variabel*.csv"):
            csv_path = file
            break
    
    if csv_path is None:
        raise FileNotFoundError(
            "File CSV tidak ditemukan. Pastikan 'UTS OS KEL 6 - variabel.csv' "
            "berada di folder yang sama dengan app.py"
        )
    
    # BACA CSV - SEMUA SEBAGAI STRING DULU
    df = pd.read_csv(csv_path, sep=';', dtype=str)
    
    # PERBAIKAN UNTUK KOLOM TAHUN
    if 'tahun' in df.columns:
        # Hapus SEMUA karakter non-digit dari kolom tahun
        df['tahun'] = df['tahun'].str.replace(r'[^\d]', '', regex=True)
        # Konversi ke integer
        df['tahun'] = df['tahun'].astype(int)
    
    return df

@st.cache_data
def preprocess_data(df):
    """Preprocessing data"""
    df_processed = df.copy()
    
    # ============================================
    # PAKSA TAHUN JADI INTEGER MURNI
    # ============================================
    if 'tahun' in df_processed.columns:
        # Konversi ke integer paksa
        df_processed['tahun'] = pd.to_numeric(df_processed['tahun'], errors='coerce').fillna(0).astype(int)
    
    num_cols = ['rls', 'hls', 'amh', 'apm_ma', 'apk', 'persen_penduduk_ma']
    
    for col in num_cols:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].astype(str).str.replace(',', '.')
            df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')
    
    return df_processed

def get_unique_years(df):
    return sorted(df['tahun'].unique())

def get_unique_regions(df):
    return sorted(df['namobj'].unique())

def filter_data(df, years=None, regions=None):
    filtered_df = df.copy()
    if years:
        filtered_df = filtered_df[filtered_df['tahun'].isin(years)]
    if regions:
        filtered_df = filtered_df[filtered_df['namobj'].isin(regions)]
    return filtered_df