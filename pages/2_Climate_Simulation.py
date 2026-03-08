import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


# ---------- SIDEBAR ----------
st.sidebar.title("🌍 Climate Dashboard")

st.sidebar.markdown("""
### Navigation
Use the menu below to explore the dashboard.
""")


st.title("🌦 Climate Simulation Tool")

st.write("""
This tool allows users to explore how climate variables influence each other.
Select a variable to predict and adjust the other factors to estimate the outcome.
""")

st.divider()

# ---------- LOAD DATA ----------
data = pd.read_csv("mumbai_weather_data_2010_2023.csv")

# ---------- SELECT TARGET ----------
target = st.selectbox(
    "Select parameter to predict",
    ["Humidity(%)", "Temperature(C)", "Precipitation(mm)"]
)

# ---------- DEFINE FEATURES ----------
if target == "Humidity(%)":
    features = ["Temperature(C)", "Precipitation(mm)"]

elif target == "Temperature(C)":
    features = ["Humidity(%)", "Precipitation(mm)"]

else:
    features = ["Temperature(C)", "Humidity(%)"]

# ---------- TRAIN MODEL ----------
X = data[features]
y = data[target]

model = LinearRegression()
model.fit(X, y)

st.subheader("Adjust Climate Factors")

input_values = {}

for feature in features:
    
    min_val = float(data[feature].min())
    max_val = float(data[feature].max())
    mean_val = float(data[feature].mean())

    input_values[feature] = st.slider(
        feature,
        min_value=float(min_val),
        max_value=float(max_val),
        value=float(mean_val)
    )

# ---------- PREDICTION ----------
prediction = model.predict([[input_values[features[0]], input_values[features[1]]]])

st.divider()

st.subheader("🌡 Predicted Value")

st.metric(
    label=f"Predicted {target}",
    value=round(prediction[0],2)
)

st.divider()

# ---------- INTERPRETATION ----------
st.subheader("📌 Interpretation")

if target == "Humidity(%)":
    st.write(f"""
Based on the selected temperature and rainfall values,
the predicted humidity level is **{round(prediction[0],2)}%**.

Higher rainfall and temperature generally increase atmospheric moisture,
which can lead to higher humidity levels.
""")

elif target == "Temperature(C)":
    st.write(f"""
Based on the selected humidity and rainfall conditions,
the predicted temperature is **{round(prediction[0],2)}°C**.

Humidity and rainfall patterns can influence temperature through
evaporation, cloud cover, and atmospheric conditions.
""")

else:
    st.write(f"""
Based on the selected temperature and humidity conditions,
the predicted rainfall is **{round(prediction[0],2)} mm**.

Higher humidity and warm temperatures often contribute to
increased rainfall due to stronger atmospheric moisture cycles.
""")

st.divider()

st.success("""
This simulation uses a simple linear regression model trained on the dataset.
It estimates how climate variables may influence each other.
""")