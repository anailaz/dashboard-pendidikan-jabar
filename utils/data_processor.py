"""
Data processor untuk perhitungan dan agregasi data
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def get_summary_stats(df, year=None):
    """
    Mendapatkan statistik ringkasan
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        year (int): Tahun spesifik (opsional)
        
    Returns:
        pd.DataFrame: Statistik deskriptif
    """
    if year:
        data = df[df['tahun'] == year]
    else:
        data = df
    
    num_cols = ['rls', 'hls', 'amh', 'apm_ma', 'apk', 'persen_penduduk_ma']
    
    stats = data[num_cols].describe().round(2)
    return stats

def calculate_yearly_growth(df, indicator):
    """
    Menghitung pertumbuhan tahunan per wilayah
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        indicator (str): Nama indikator
        
    Returns:
        pd.DataFrame: DataFrame dengan kolom pertumbuhan
    """
    pivot = df.pivot(index='namobj', columns='tahun', values=indicator)
    
    # Hitung pertumbuhan tahunan
    growth = pivot.pct_change(axis=1) * 100
    
    return growth

def get_top_regions(df, indicator, year, n=5, ascending=False):
    """
    Mendapatkan top n wilayah berdasarkan indikator
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        indicator (str): Nama indikator
        year (int): Tahun
        n (int): Jumlah wilayah
        ascending (bool): Urutan ascending/descending
        
    Returns:
        list: Daftar nama wilayah
    """
    data_year = df[df['tahun'] == year]
    top_regions = data_year.nlargest(n, indicator)['namobj'].tolist() if not ascending \
                  else data_year.nsmallest(n, indicator)['namobj'].tolist()
    
    return top_regions

def get_bottom_regions(df, indicator, year, n=5):
    """
    Mendapatkan n wilayah terendah berdasarkan indikator
    """
    return get_top_regions(df, indicator, year, n, ascending=True)

def calculate_regional_disparity(df, indicator, year):
    """
    Menghitung disparitas regional (rasio max/min)
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        indicator (str): Nama indikator
        year (int): Tahun
        
    Returns:
        float: Rasio disparitas
    """
    data_year = df[df['tahun'] == year]
    max_val = data_year[indicator].max()
    min_val = data_year[indicator].min()
    
    return max_val / min_val if min_val > 0 else 0

def prepare_clustering_data(df, year):
    """
    Menyiapkan data untuk clustering
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        year (int): Tahun
        
    Returns:
        tuple: (scaled_data, original_data)
    """
    data_year = df[df['tahun'] == year].copy()
    
    # Fitur untuk clustering
    features = ['rls', 'hls', 'amh', 'apm_ma', 'apk', 'persen_penduduk_ma']
    
    X = data_year[features].values
    
    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, data_year

def perform_clustering(X_scaled, n_clusters=3, random_state=42):
    """
    Melakukan K-Means clustering
    
    Args:
        X_scaled (np.array): Data yang sudah di-scale
        n_clusters (int): Jumlah cluster
        random_state (int): Random seed
        
    Returns:
        tuple: (labels, kmeans_model)
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    return labels, kmeans

def assign_cluster_labels(labels, data):
    """
    Memberikan label kategori pada cluster
    
    Args:
        labels (np.array): Hasil clustering
        data (pd.DataFrame): Data original
        
    Returns:
        list: Label kategori (Rendah/Sedang/Tinggi)
    """
    # Hitung rata-rata RLS per cluster
    cluster_means = {}
    for i in range(3):
        mask = labels == i
        cluster_means[i] = data.loc[mask, 'rls'].mean()
    
    # Urutkan cluster berdasarkan rata-rata RLS
    sorted_clusters = sorted(cluster_means.items(), key=lambda x: x[1])
    
    # Mapping label
    label_map = {
        sorted_clusters[0][0]: 'Rendah',
        sorted_clusters[1][0]: 'Sedang',
        sorted_clusters[2][0]: 'Tinggi'
    }
    
    return [label_map[label] for label in labels]