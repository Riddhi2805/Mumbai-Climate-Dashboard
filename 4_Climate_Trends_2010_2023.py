import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ---------- SIDEBAR ----------
st.sidebar.title("🌍 Climate Dashboard")

st.sidebar.markdown("""
### Navigation
Use the menu below to explore the dashboard.
""")


st.title("📈 Climate Changes in Mumbai (2010–2023)")

st.write("""
This section analyzes how climate variables in Mumbai have changed
between 2010 and 2023 using historical climate data.
""")

st.divider()

# ---------- LOAD DATA ----------
data = pd.read_csv("mumbai_weather_data_2010_2023.csv")

data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")
data["Year"] = data["Date"].dt.year

# ---------- YEARLY AVERAGES ----------
yearly = data.groupby("Year").mean(numeric_only=True)

# ---------- TEMPERATURE TREND ----------
st.subheader("🌡 Temperature Change Over Years")

fig, ax = plt.subplots()
ax.plot(yearly.index, yearly["Temperature(C)"], marker="o", color="red")

ax.set_xlabel("Year")
ax.set_ylabel("Average Temperature (°C)")
ax.set_title("Temperature Trend (2010–2023)")

st.pyplot(fig)

st.info("This graph shows how average yearly temperature has changed over time.")

st.divider()

# ---------- RAINFALL TREND ----------
st.subheader("🌧 Rainfall Change Over Years")

fig, ax = plt.subplots()
ax.plot(yearly.index, yearly["Precipitation(mm)"], marker="o", color="blue")

ax.set_xlabel("Year")
ax.set_ylabel("Average Rainfall (mm)")
ax.set_title("Rainfall Trend (2010–2023)")

st.pyplot(fig)

st.info("This graph shows yearly variations in rainfall levels.")

st.divider()

# ---------- HUMIDITY TREND ----------
st.subheader("💧 Humidity Change Over Years")

fig, ax = plt.subplots()
ax.plot(yearly.index, yearly["Humidity(%)"], marker="o", color="green")

ax.set_xlabel("Year")
ax.set_ylabel("Average Humidity (%)")
ax.set_title("Humidity Trend (2010–2023)")

st.pyplot(fig)

st.info("Humidity trends reflect moisture levels in the atmosphere over time.")

st.divider()

# ---------- SEA LEVEL ----------
st.subheader("🌊 Sea Level Rise Trend")

fig, ax = plt.subplots()
ax.plot(yearly.index, yearly["Sea_Level_Rise(mm)"], marker="o", color="purple")

ax.set_xlabel("Year")
ax.set_ylabel("Sea Level Rise (mm)")
ax.set_title("Sea Level Change (2010–2023)")

st.pyplot(fig)

st.info("Sea level changes are important indicators of long-term climate change.")

st.divider()

# ---------- CALCULATE CHANGES ----------
temp_change = yearly["Temperature(C)"].iloc[-1] - yearly["Temperature(C)"].iloc[0]
rain_change = yearly["Precipitation(mm)"].iloc[-1] - yearly["Precipitation(mm)"].iloc[0]
humidity_change = yearly["Humidity(%)"].iloc[-1] - yearly["Humidity(%)"].iloc[0]
sea_change = yearly["Sea_Level_Rise(mm)"].iloc[-1] - yearly["Sea_Level_Rise(mm)"].iloc[0]

# ---------- INTERPRETATION ----------
st.subheader("📌 Climate Change Interpretation (2010–2023)")

st.success(f"""
• Average **temperature changed by {temp_change:.2f} °C** between 2010 and 2023.

• Average **rainfall changed by {rain_change:.2f} mm** during this period.

• Average **humidity changed by {humidity_change:.2f}%**.

• **Sea level changed by {sea_change:.2f} mm**, which may indicate long-term climate shifts.

Overall, the dataset suggests noticeable changes in climate variables
over the 13-year period. These variations highlight the importance
of monitoring climate trends, especially in coastal cities like Mumbai.
""")

st.divider()

st.subheader("⚠ Climate Impact Assessment")

positive_impacts = []
negative_impacts = []

# Temperature impacts
if temp_change > 0:
    negative_impacts.append("Rising temperatures may increase heat stress and energy demand for cooling.")
else:
    positive_impacts.append("Lower temperatures may reduce heat stress in urban environments.")

# Rainfall impacts
if rain_change > 0:
    positive_impacts.append("Increased rainfall may improve water availability and groundwater recharge.")
    negative_impacts.append("Excess rainfall may increase flood risk in low-lying areas.")
else:
    negative_impacts.append("Reduced rainfall may lead to water scarcity and drought conditions.")

# Humidity impacts
if humidity_change > 0:
    negative_impacts.append("Higher humidity may increase discomfort and risk of certain diseases.")
else:
    positive_impacts.append("Lower humidity levels may improve thermal comfort.")

# Sea level impacts
if sea_change > 0:
    negative_impacts.append("Rising sea levels may increase coastal flooding risks in Mumbai.")

# ---------- DISPLAY ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Potential Positive Impacts")
    
    if positive_impacts:
        for impact in positive_impacts:
            st.success(impact)
    else:
        st.write("No significant positive impacts identified.")

with col2:
    st.subheader("⚠ Potential Negative Impacts")
    
    if negative_impacts:
        for impact in negative_impacts:
            st.error(impact)
    else:
        st.write("No significant negative impacts identified.")