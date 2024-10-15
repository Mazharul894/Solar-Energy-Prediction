import streamlit as st
import joblib
import pandas as pd

# Load the trained Random Forest model
model_path = "D:/Solar Energy/random_forest_model.pkl"
model = joblib.load(model_path)

# Solar panel parameters
solar_panel_efficiency = 0.2  # 20%
solar_panel_area_sq_m = 1.70429  # in square meters

# Function to predict radiation and calculate solar power output
def predict_radiation_and_calculate_solar_power(temp, pressure, humidity, wind_direction, wind_speed, time_seconds, sunrise_seconds, sunset_seconds):
    # Prepare input data
    input_data = pd.DataFrame({
        'Temperature': [temp],
        'Pressure': [pressure],
        'Humidity': [humidity],
        'WindDirection(Degrees)': [wind_direction],
        'Speed': [wind_speed],
        'Time In Seconds': [time_seconds],
        'Sun Rise In Seconds': [sunrise_seconds],
        'Sun Set In Seconds': [sunset_seconds]
    })

    # Make predictions
    predicted_radiation = model.predict(input_data)

    # Calculate solar power output
    solar_power_output_kwh = predicted_radiation * solar_panel_efficiency * solar_panel_area_sq_m

    return predicted_radiation[0], solar_power_output_kwh[0]

# Streamlit app
def main():
    st.title("Solar Power Output Prediction")

    st.sidebar.header("Input Parameters")
    temperature = st.sidebar.slider("Temperature (°C)", -20, 50)
    pressure = st.sidebar.slider("Pressure (mbar)", 800.0, 1100.0, step=0.1)
    humidity = st.sidebar.slider("Humidity (%)", 0, 100)
    wind_direction = st.sidebar.slider("Wind Direction (Degrees)", 0.0, 360.0)
    wind_speed = st.sidebar.slider("Wind Speed (m/s)", 0.0, 10.0)
    time_seconds = st.sidebar.number_input("Time In Seconds", value=0)
    sunrise_seconds = st.sidebar.number_input("Sun Rise In Seconds", value=0)
    sunset_seconds = st.sidebar.number_input("Sun Set In Seconds", value=0)

    if st.sidebar.button("Predict Radiation and Calculate Solar Power Output"):
        predicted_radiation, solar_power_output = predict_radiation_and_calculate_solar_power(
            temperature, pressure, humidity, wind_direction, wind_speed, time_seconds, sunrise_seconds, sunset_seconds
        )
        st.write(f"Predicted Radiation: {predicted_radiation}")
        st.write(f"Solar Power Output (kWh): {solar_power_output}")

if __name__ == "__main__":
    main()
