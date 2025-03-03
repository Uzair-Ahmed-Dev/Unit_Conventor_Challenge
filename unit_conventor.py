import streamlit as st

# Conversion factors (simplified, you can expand)
CONVERSION_FACTORS = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371,
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1_000_000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    },
    "Temperature": {
        "Celsius": "temp",
        "Fahrenheit": "temp",
        "Kelvin": "temp",
    }
}

# Function to convert length and weight units
def convert_units(value, from_unit, to_unit, unit_type):
    if from_unit == to_unit:
        return value
    factor_from = CONVERSION_FACTORS[unit_type][from_unit]
    factor_to = CONVERSION_FACTORS[unit_type][to_unit]
    return value * (factor_to / factor_from)

# Function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # fallback (shouldn’t hit this)

# Streamlit UI
st.title("Google-style Unit Converter 🌐")

# Dropdown for measurement type
unit_type = st.selectbox("Select Measurement Type", list(CONVERSION_FACTORS.keys()))

# Dropdowns for units
if unit_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
else:
    units = list(CONVERSION_FACTORS[unit_type].keys())

from_unit = st.selectbox("Convert From", units)
to_unit = st.selectbox("Convert To", units)

# Input value
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

# Conversion logic
if unit_type == "Temperature":
    result = convert_temperature(value, from_unit, to_unit)
else:
    result = convert_units(value, from_unit, to_unit, unit_type)

# Display result
st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
