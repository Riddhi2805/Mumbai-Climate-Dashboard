import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ---------- SIDEBAR ----------
st.sidebar.title("🌍 Climate Dashboard")

st.sidebar.markdown("""
### Navigation
Use the menu below to explore the dashboard.
""")


# ---------- PAGE TITLE ----------

st.title("Mumbai Climate Data Analysis")

# Load dataset
data = pd.read_csv("mumbai_weather_data_2010_2023.csv")

# Convert date column
data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")

# Extract year and month
data["Year"] = data["Date"].dt.year
data["Month"] = data["Date"].dt.month

# Year filter
year = st.selectbox("Select Year", sorted(data["Year"].unique()))

filtered = data[data["Year"] == year]

# Dataset preview
st.subheader("Dataset Preview")
st.write(filtered.head())

# --------------------------------
# Temperature Trend
# --------------------------------

st.subheader("Temperature Trend")

fig, ax = plt.subplots()
ax.plot(filtered["Month"], filtered["Temperature(C)"], marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Monthly Temperature Trend")

st.pyplot(fig)

st.info("""
Interpretation:
This graph shows how temperature changes throughout the year.
Higher temperatures usually occur during summer months,
while lower temperatures appear during winter.
This helps identify seasonal temperature patterns in Mumbai.
""")

# --------------------------------
# Rainfall Trend
# --------------------------------

st.subheader("Rainfall Trend")

fig, ax = plt.subplots()
ax.bar(filtered["Month"], filtered["Precipitation(mm)"])
ax.set_xlabel("Month")
ax.set_ylabel("Rainfall (mm)")
ax.set_title("Monthly Rainfall")

st.pyplot(fig)

st.info("""
Interpretation:
This chart shows rainfall distribution across the months.
Rainfall generally peaks during the monsoon season
(June to September) in Mumbai.
""")

# --------------------------------
# Humidity Trend
# --------------------------------

st.subheader("Humidity Trend")

fig, ax = plt.subplots()
ax.plot(filtered["Month"], filtered["Humidity(%)"], marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Humidity (%)")
ax.set_title("Monthly Humidity")

st.pyplot(fig)

st.info("""
Interpretation:
Humidity represents the amount of moisture in the air.
Higher humidity levels are commonly observed during monsoon months
and can influence rainfall patterns.
""")

# --------------------------------
# GHG Emissions Trend
# --------------------------------

st.subheader("GHG Emissions Trend")

fig, ax = plt.subplots()
ax.plot(filtered["Month"], filtered["GHG_Emissions(metric_tons_per_capita)"], marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("GHG Emissions")
ax.set_title("Monthly Greenhouse Gas Emissions")

st.pyplot(fig)

st.info("""
Interpretation:
This graph shows variation in greenhouse gas emissions.
Higher emissions can contribute to long-term climate change
and rising global temperatures.
""")

# --------------------------------
# Correlation Matrix
# --------------------------------

st.subheader("Correlation Between Climate Variables")

numeric_data = filtered.select_dtypes(include="number")

corr = numeric_data.corr()

st.dataframe(corr)

st.info("""
Interpretation:
The correlation matrix shows relationships between climate variables.
Values close to +1 indicate strong positive relationships,
while values near -1 indicate negative relationships.
This helps understand how climate factors influence each other.
""")
