"""
Komponen reusable untuk visualisasi
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import streamlit as st
from config.settings import COLORS, CLUSTER_COLORS

def create_line_chart(df, x, y, color, title, labels, height=500):
    """
    Membuat line chart dengan Plotly
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        x (str): Kolom untuk sumbu x
        y (str): Kolom untuk sumbu y
        color (str): Kolom untuk warna
        title (str): Judul chart
        labels (dict): Label untuk axes
        height (int): Tinggi chart
        
    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        markers=True,
        title=title,
        labels=labels,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_layout(
        height=height,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend_title_text='Wilayah',
        font=dict(family='Inter, sans-serif')
    )
    
    return fig

def create_line_chart_with_dropdown(df, x, y, color, title, labels, 
                                     top_n_options, default_top_n=5):
    """
    Membuat line chart dengan dropdown untuk filter top N
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        x (str): Kolom untuk sumbu x
        y (str): Kolom untuk sumbu y
        color (str): Kolom untuk warna
        title (str): Judul chart
        labels (dict): Label untuk axes
        top_n_options (list): Daftar opsi top N
        default_top_n (int): Default top N
        
    Returns:
        plotly.graph_objects.Figure
    """
    # Dapatkan top N wilayah berdasarkan tahun terakhir
    last_year = df['tahun'].max()
    df_last = df[df['tahun'] == last_year].sort_values(y, ascending=False)
    
    fig = go.Figure()
    
    # Tambah trace untuk semua wilayah (hidden by default)
    for region in df[color].unique():
        region_data = df[df[color] == region]
        
        fig.add_trace(go.Scatter(
            x=region_data[x],
            y=region_data[y],
            name=region,
            mode='lines+markers',
            visible=False
        ))
    
    # Buat dropdown buttons
    buttons = []
    
    for n in top_n_options:
        top_regions = df_last.head(n)[color].tolist()
        
        visibility = [trace.name in top_regions for trace in fig.data]
        
        buttons.append(dict(
            label=f'Top {n} Wilayah',
            method='update',
            args=[{'visible': visibility},
                  {'title': f'{title} - Top {n} Wilayah'}]
        ))
    
    # Tambah opsi semua wilayah
    buttons.append(dict(
        label='Semua Wilayah',
        method='update',
        args=[{'visible': [True] * len(fig.data)},
              {'title': f'{title} - Semua Wilayah'}]
    ))
    
    # Set default visibility (Top 5)
    default_top = df_last.head(default_top_n)[color].tolist()
    for trace in fig.data:
        trace.visible = trace.name in default_top
    
    # Update layout
    fig.update_layout(
        updatemenus=[dict(
            active=0,
            buttons=buttons,
            x=1.15,
            y=1.15,
            xanchor='right',
            yanchor='top'
        )],
        height=500,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend_title_text='Wilayah',
        font=dict(family='Inter, sans-serif')
    )
    
    fig.update_xaxes(title_text=labels.get(x, x))
    fig.update_yaxes(title_text=labels.get(y, y))
    
    return fig

def create_animated_bar_chart(df, x, y, animation_frame, color_by_rank=True):
    """
    Membuat animated bar chart untuk perbandingan antar tahun
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        x (str): Kolom nilai (sumbu x)
        y (str): Kolom kategori (sumbu y)
        animation_frame (str): Kolom untuk animasi (tahun)
        color_by_rank (bool): Apakah mewarnai berdasarkan ranking
        
    Returns:
        plotly.graph_objects.Figure
    """
    df_bar = df.copy()
    
    if color_by_rank:
        # Tandai top 5 per tahun
        df_bar['status_warna'] = 0
        
        for year in df_bar[animation_frame].unique():
            top5 = df_bar[df_bar[animation_frame] == year].nlargest(5, x)['namobj'].tolist()
            mask = (df_bar[animation_frame] == year) & (df_bar['namobj'].isin(top5))
            df_bar.loc[mask, 'status_warna'] = 1
        
        color_col = 'status_warna'
        color_map = {0: COLORS['secondary'], 1: COLORS['accent']}
    else:
        color_col = None
        color_map = None
    
    # Urutkan berdasarkan nilai tahun terakhir
    last_year = df_bar[animation_frame].max()
    y_order = df_bar[df_bar[animation_frame] == last_year].sort_values(x, ascending=True)['namobj'].tolist()
    
    fig = px.bar(
        df_bar,
        x=x,
        y=y,
        color=color_col,
        animation_frame=animation_frame,
        animation_group=y,
        orientation='h',
        title='Persentase Penduduk Minimal SMA di Jawa Barat',
        labels={x: 'Persentase (%)', y: 'Kabupaten/Kota'},
        color_discrete_map=color_map if color_map else None,
        range_x=[0, df_bar[x].max() + 5]
    )
    
    fig.update_layout(
        height=700,
        yaxis={'categoryorder': 'array', 'categoryarray': y_order},
        hovermode='y unified',
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter, sans-serif')
    )
    
    # Atur durasi animasi
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1500
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    
    return fig

def create_cluster_scatter(df, x, y, color, animation_frame, text, 
                           hover_data, title):
    """
    Membuat scatter plot untuk visualisasi clustering
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        x (str): Kolom sumbu x
        y (str): Kolom sumbu y
        color (str): Kolom warna (cluster)
        animation_frame (str): Kolom animasi (tahun)
        text (str): Kolom teks label
        hover_data (dict): Data untuk hover
        title (str): Judul chart
        
    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        animation_frame=animation_frame,
        animation_group=text,
        text=text,
        hover_name=text,
        hover_data=hover_data,
        color_discrete_map=CLUSTER_COLORS,
        size_max=15,
        title=title
    )
    
    fig.update_traces(
        textposition='top center',
        marker=dict(size=14, line=dict(width=1, color='white')),
        textfont=dict(size=9)
    )
    
    fig.update_layout(
        xaxis_title='Rata-rata Lama Sekolah (tahun)',
        yaxis_title='Persentase Penduduk Minimal SMA (%)',
        legend_title_text='Cluster',
        height=600,
        hovermode='closest',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter, sans-serif')
    )
    
    # Atur durasi animasi
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1500
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    
    return fig

def create_stacked_bar_chart(df, x, y, color, text, title, labels):
    """
    Membuat stacked bar chart
    
    Args:
        df (pd.DataFrame): DataFrame sumber
        x (str): Kolom sumbu x
        y (str): Kolom nilai
        color (str): Kolom warna
        text (str): Kolom teks label
        title (str): Judul chart
        labels (dict): Label untuk axes
        
    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        text=text,
        title=title,
        labels=labels,
        color_discrete_map=CLUSTER_COLORS,
        category_orders={'cluster': ['Rendah', 'Sedang', 'Tinggi']}
    )
    
    fig.update_layout(
        barmode='stack',
        height=500,
        xaxis_type='category',
        hovermode='x unified',
        legend_title_text='Status Cluster',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter, sans-serif')
    )
    
    fig.update_traces(textfont_size=14, textposition="inside")
    
    return fig