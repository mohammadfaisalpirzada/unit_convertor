import streamlit as st

# Streamlit App Title
st.title("🌍 Master Sahub Universal Unit Converter")

# Comprehensive Unit Categories
categories = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight/Mass": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274,
        "Ton": 0.001, "Stone": 0.157473
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    },
    "Time": {
        "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400,
        "Week": 1/604800, "Month": 1/2.628e+6, "Year": 1/3.154e+7
    },
    "Speed": {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694,
        "Knots": 1.94384, "Mach": 0.002938
    },
    "Volume": {
        "Liter": 1, "Milliliter": 1000, "Cubic meter": 0.001, "Cups": 4.16667,
        "Pint": 2.11338, "Gallon": 0.264172
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 1e-6, "Acre": 0.000247105,
        "Hectare": 1e-4, "Square Foot": 10.7639
    },
    "Pressure": {
        "Pascal": 1, "Bar": 1e-5, "PSI": 0.000145038, "mmHg": 0.00750062,
        "Atmosphere": 9.8692e-6
    },
    "Energy": {
        "Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilocalorie": 0.000239006,
        "Watt-hour": 0.000277778
    },
    "Power": {
        "Watt": 1, "Kilowatt": 0.001, "Horsepower": 0.00134102, "BTU/hr": 3.41214
    },
    "Digital Storage": {
        "Bit": 1, "Byte": 0.125, "Kilobyte": 0.00012207, "Megabyte": 1.1921e-7,
        "Gigabyte": 1.1642e-10, "Terabyte": 1.1369e-13
    },
    "Fuel Economy": {
        "km/L": 1, "mpg": 2.35215, "L/100km": 235.215
    },
    "Force": {
        "Newton": 1, "Dyne": 100000, "Pound-force": 0.224809, "Kilogram-force": 0.101972
    },
    "Frequency": {
        "Hertz": 1, "Kilohertz": 0.001, "Megahertz": 1e-6, "Gigahertz": 1e-9
    },
    "Angle": {
        "Degree": 1, "Radian": 0.0174533, "Gradian": 1.11111
    }
}

# Sidebar for better UI
st.sidebar.header("⚙️ Settings")
category = st.sidebar.selectbox("Select a category", list(categories.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert From", list(categories[category].keys()))
with col2:
    to_unit = st.selectbox("Convert To", list(categories[category].keys()))

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")


# Conversion function
def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value
    else:
        return value * (categories[category][to_unit] / categories[category][from_unit])


# Perform conversion dynamically
if from_unit == to_unit:
    st.info("Please select different units for conversion.")
else:
    result = convert(value, from_unit, to_unit, category)
    st.success(f"✅ {value:.2f} {from_unit} = {result:.2f} {to_unit}")
