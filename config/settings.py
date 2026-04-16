"""
Konfigurasi global untuk dashboard
"""

# Color palette BARU
COLORS = {
    "primary": "#7DAACB",      # Biru muda
    "secondary": "#E8DBB3",    # Krem
    "accent": "#CE2626",       # Merah
    "background": "#FFFDEB",   # Krem putih
    "white": "#FFFFFF",
    "text_dark": "#000000",    # Hitam untuk semua teks
    "text_light": "#333333",   # Abu-abu gelap (tetap terbaca)
    "sidebar_bg": "#7DAACB",   # Warna sidebar
}

# Mapping cluster colors (disesuaikan dengan palette baru)
CLUSTER_COLORS = {
    'Rendah': '#CE2626',       # Merah (accent)
    'Sedang': '#7DAACB',       # Biru muda (primary)
    'Tinggi': '#E8DBB3',       # Krem (secondary)
}

# Daftar indikator
INDICATORS = {
    'rls': 'Rata-rata Lama Sekolah (tahun)',
    'hls': 'Harapan Lama Sekolah (tahun)',
    'amh': 'Angka Melek Huruf (%)',
    'apm_ma': 'APM MA (%)',
    'apk': 'APK (%)',
    'persen_penduduk_ma': 'Persentase Penduduk Minimal SMA (%)'
}