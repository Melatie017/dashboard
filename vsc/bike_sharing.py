import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

# Fungsi untuk mengambil data
def load_data():
    # Gantilah 'path_to_hour_df' dengan lokasi file hour_df.csv
    hour_df = pd.read_csv('https://raw.githubusercontent.com/Melatie017/dashboard/main/vsc/dataku.csv')
    return hour_df

# Memuat data
hour_df = load_data()

# Judul aplikasi
st.markdown("""
    <h1 style='text-align: center;'>Bike Sharing Dashboard</h1>
""", unsafe_allow_html=True)

#Pada season dan bulan apa orang-orang paling banyak melakukan peminjaman?
st.markdown("""
    <h3 style='text-align: center;'>Rata-Rata Peminjam Sepeda per Bulan</h3>
""", unsafe_allow_html=True)

# Menghitung rata-rata jumlah peminjam sepeda berdasarkan bulan
avg_cnt_by_month = hour_df.groupby('mnth')['cnt'].mean()

# Mengatur urutan bulan
order = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
avg_cnt_by_month = avg_cnt_by_month.reindex(index=order)

# Memvisualisasikan rata-rata jumlah peminjam sepeda per bulan sebagai line chart
plt.figure(figsize=(10, 6))
plt.plot(avg_cnt_by_month.index, avg_cnt_by_month.values, marker='o', color='darkgreen', linestyle='-')
plt.xlabel('Bulan')
plt.ylabel('Rata-Rata Jumlah Peminjam')
plt.xticks(rotation=45)
st.pyplot(plt)

st.markdown("""
    <h3 style='text-align: center;'>Informasi Tanggal dan Bulan Sesuai 4 Musim</h3>
""", unsafe_allow_html=True)
st.text('**Spring** = 21 Desember - 20 Maret')
st.text('**Summer** = 21 Maret - 20 Juni')
st.text('**Fall** = 21 Juni - 22 September')
st.text('**Winter** = 23 September - 20 Desember')



#Berapa persen perbandingan pengguna yang casual dengan yang terdaftar?
st.markdown("""
    <h3 style='text-align: center;'>Persentase Jumlah Peminjam Casual dan Registered</h3>
""", unsafe_allow_html=True)

# Menghitung jumlah peminjam casual dan registered
jumlah_casual = hour_df['casual'].sum()
jumlah_registered = hour_df['registered'].sum()
explode = (0, 0.1)  # Menonjolkan bagian registered

# Memvisualisasikan perbandingan jumlah peminjam casual dan registered dalam pie chart
fig, ax = plt.subplots()
ax.pie([jumlah_casual, jumlah_registered], labels=['Casual', 'Registered'], explode=explode, autopct='%1.1f%%', shadow=True, startangle=140, colors=['darkgreen', 'lightgreen'])
ax.axis('equal')  # Membuat pie chart menjadi lingkaran
st.pyplot(fig)



#Pada suhu berapa orang-orang banyak beraktivitas diluar?
st.markdown("""
    <h3 style='text-align: center;'>Rata-Rata Peminjam Sepeda per Suhu</h3>
""", unsafe_allow_html=True)

# Menghitung rata-rata jumlah peminjam sepeda berdasarkan suhu
rata_rata_cnt_per_suhu = hour_df.groupby('temp')['cnt'].mean()

# Menampilkan data dalam bentuk bar plot
plt.figure(figsize=(30, 17))
rata_rata_cnt_per_suhu.plot(kind='bar', color='darkgreen')
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Rata-Rata Jumlah Peminjam')
plt.xticks(rotation=45)
st.pyplot(plt)
