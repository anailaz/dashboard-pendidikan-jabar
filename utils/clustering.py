"""
Modul clustering
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import streamlit as st

@st.cache_data
def perform_clustering_all_years(df, years=range(2021, 2026), n_clusters=3):
    """Melakukan clustering untuk semua tahun"""
    
    features = ['rls', 'hls', 'amh', 'apm_ma', 'apk', 'persen_penduduk_ma']
    regions = df['namobj'].unique()
    cluster_results = pd.DataFrame(index=regions)
    
    for year in years:
        data_year = df[df['tahun'] == year].set_index('namobj')
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(data_year[features])
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        
        # Assign label kategori
        cluster_means = {}
        for i in range(n_clusters):
            mask = labels == i
            cluster_means[i] = data_year.iloc[mask]['rls'].mean()
        
        sorted_clusters = sorted(cluster_means.items(), key=lambda x: x[1])
        label_map = {
            sorted_clusters[0][0]: 'Rendah',
            sorted_clusters[1][0]: 'Sedang',
            sorted_clusters[2][0]: 'Tinggi'
        }
        
        categorical_labels = [label_map[label] for label in labels]
        cluster_results[f'cluster_{year}'] = categorical_labels
    
    return cluster_results

def get_cluster_summary(cluster_results):
    """Ringkasan jumlah wilayah per cluster"""
    df = cluster_results.drop('Silhouette Score', errors='ignore')
    years = [col for col in df.columns if col.startswith('cluster_')]
    
    summary_data = []
    for year in years:
        year_num = year.split('_')[1]
        value_counts = df[year].value_counts()
        
        for cluster, count in value_counts.items():
            summary_data.append({
                'tahun': year_num,
                'cluster': cluster,
                'jumlah_wilayah': count
            })
    
    return pd.DataFrame(summary_data)