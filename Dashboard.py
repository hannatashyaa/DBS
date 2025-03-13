import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("https://raw.githubusercontent.com/hannatashyaa/bike/refs/heads/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/hannatashyaa/bike/refs/heads/main/hour.csv")

# Convert date column
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Mapping musim berdasarkan kode
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day_df['season_name'] = day_df['season'].map(season_map)

# Sidebar Filters
st.sidebar.header("Filter Data")

# Date range filter
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()
start_date, end_date = st.sidebar.date_input("Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])

# Filter berdasarkan rentang tanggal
filtered_day_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date))]
filtered_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & (hour_df["dteday"] <= pd.to_datetime(end_date))]

# Dashboard Title
st.title("Bike Sharing Analysis Dashboard")

# **Daily Orders**
st.subheader("Daily Orders")

col1, col2 = st.columns(2)

with col1:
    total_orders = filtered_day_df['cnt'].sum()
    st.metric("Total Orders", value=total_orders)

with col2:
    total_revenue = total_orders * 5  # Anggap harga sewa per unit = $5
    st.metric("Total Revenue (USD)", value=f"${total_revenue:,.2f}")

# Plot Daily Orders
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(
    filtered_day_df["dteday"],
    filtered_day_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.set_xlabel("Tanggal", fontsize=12)
ax.set_ylabel("Jumlah Penyewaan", fontsize=12)
ax.set_title("Tren Daily Orders", fontsize=14)
ax.grid(True)
st.pyplot(fig)

# **Musim yang Terdeteksi**
if not filtered_day_df.empty:
    detected_seasons = filtered_day_df['season_name'].unique()
    detected_seasons_str = ", ".join(sorted(detected_seasons))
else:
    detected_seasons_str = "Tidak ada data dalam rentang tanggal yang dipilih"

st.subheader(f"Musim yang terdeteksi: {detected_seasons_str}")

# **Total Penyewaan Berdasarkan Musim**
st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")
if not filtered_day_df.empty:
    season_rentals = filtered_day_df.groupby("season_name")["cnt"].sum()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=season_rentals.index, y=season_rentals.values, palette="Blues")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penyewaan")
    plt.title("Total Penyewaan Sepeda per Musim")
    st.pyplot(plt)
else:
    st.write("Tidak ada data yang tersedia untuk ditampilkan.")

# **Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari**
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
plt.figure(figsize=(10, 5))
hourly_rentals = filtered_hour_df.groupby("hr")["cnt"].sum()
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", linestyle="-", color="blue")
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewaan")
plt.title("Pola Penyewaan Sepeda per Jam")
st.pyplot(plt)

# **Manual Grouping: Kategori Waktu**
def categorize_time(hour):
    if 5 <= hour < 11:
        return "Pagi"
    elif 11 <= hour < 15:
        return "Siang"
    elif 15 <= hour < 19:
        return "Sore"
    else:
        return "Malam"

filtered_hour_df["time_category"] = filtered_hour_df["hr"].apply(categorize_time)
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Kategori Waktu")
plt.figure(figsize=(8, 5))
sns.boxplot(x="time_category", y="cnt", data=filtered_hour_df, order=["Pagi", "Siang", "Sore", "Malam"], palette="coolwarm")
plt.xlabel("Kategori Waktu")
plt.ylabel("Jumlah Peminjaman Sepeda")
plt.title("Distribusi Penyewaan Sepeda Berdasarkan Waktu")
st.pyplot(plt)

# **Binning: Kategori Jumlah Peminjaman**
bins = [0, 50, 200, filtered_hour_df["cnt"].max()]
labels = ["Rendah", "Sedang", "Tinggi"]
filtered_hour_df["cnt_category"] = pd.cut(filtered_hour_df["cnt"], bins=bins, labels=labels, include_lowest=True)

st.subheader("Distribusi Kategori Jumlah Peminjaman Sepeda")
plt.figure(figsize=(7, 5))
sns.countplot(x="cnt_category", data=filtered_hour_df, order=["Rendah", "Sedang", "Tinggi"], palette="viridis")
plt.xlabel("Kategori Peminjaman")
plt.ylabel("Jumlah Observasi")
plt.title("Distribusi Kategori Jumlah Peminjaman Sepeda")
st.pyplot(plt)

st.caption('Copyright (c) Bike Sharing Analysis 2025')
