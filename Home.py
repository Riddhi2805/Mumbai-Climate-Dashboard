import streamlit as st
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ---------- AUTO REFRESH CLOCK ----------
st_autorefresh(interval=60000)  # refresh every 1 minute

# ---------- HEADER ----------
st.title("🌍 Mumbai Climate Dashboard")

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Mumbai Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------- SIDEBAR ----------
st.sidebar.title("🌍 Climate Dashboard")

st.sidebar.markdown("""
### Navigation
Use the menu below to explore the dashboard.
""")

# ---------- BANNER IMAGE ----------
st.image("Climate_page.png", use_container_width=True)

# ---------- QUOTE ----------
st.markdown("""
<div style='text-align:center; font-size:30px; font-weight:700; color:#1B5E20; margin-top:15px;'>
🌱 “Change the trend. Save the timeline.”
</div>
""", unsafe_allow_html=True)

st.divider()


# ---------- DATE & TIME ----------
now = datetime.now()

current_date = now.strftime("%d %B %Y")
current_time = now.strftime("%H:%M:%S")

col1, col2 = st.columns(2)

col1.info(f"📅 Date: {current_date}")
col2.info(f"⏰ Time: {current_time}")

st.divider()

# ---------- LIVE WEATHER ----------
url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"

response = requests.get(url)
data = response.json()

temperature = data["current_weather"]["temperature"]
windspeed = data["current_weather"]["windspeed"]

st.subheader("🌦 Live Weather in Mumbai")

col1, col2 = st.columns(2)

col1.metric("🌡 Temperature", f"{temperature} °C")
col2.metric("💨 Wind Speed", f"{windspeed} km/h")

# ---------- WEATHER DESCRIPTION ----------
if temperature >= 35 and windspeed < 10:
    weather_desc = "Very hot and calm weather conditions are currently being experienced in Mumbai."

elif temperature >= 30 and windspeed < 15:
    weather_desc = "The weather in Mumbai is hot with light winds."

elif temperature >= 25 and windspeed >= 15:
    weather_desc = "The weather is warm but the stronger winds make it feel more comfortable."

elif temperature >= 20:
    weather_desc = "The weather is pleasant with moderate conditions."

else:
    weather_desc = "The weather is relatively cool in Mumbai today."

st.info(weather_desc)
st.divider()


# ---------- ABOUT ----------
st.subheader("About This Dashboard")

st.write("""
This dashboard analyzes climate trends in Mumbai using historical climate data.

You can explore:

• Climate Analysis  
• Climate Simulation  
• Climate Change Trends  
• User Dataset Analysis
""")