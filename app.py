import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mechanical Unit & Density Tool", layout="centered")

# --- Header & Identification ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.subheader("Student Identification")
st.info(f"**Name:** MIAN MUHAMMED MUSAAB  \n**Roll Number:** 25 ME 60")

st.divider()

# --- Material Density Checker ---
st.header("1. Material Density Checker")
material_data = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Cast Iron": 7200,
    "Concrete": 2400,
    "Water": 1000
}

selected_material = st.selectbox("Select a Material:", list(material_data.keys()))
density = material_data[selected_material]
st.write(f"The density of **{selected_material}** is **{density} kg/m³**.")

st.divider()

# --- Unit Converter ---
st.header("2. Mechanical Unit Converter")

conversion_type = st.selectbox("Select Conversion Category:", ["Length", "Pressure", "Force"])

if conversion_type == "Length":
    val = st.number_input("Enter value in Meters (m):", value=1.0)
    col1, col2 = st.columns(2)
    col1.metric("Millimeters (mm)", val * 1000)
    col2.metric("Inches (in)", round(val * 39.3701, 2))

elif conversion_type == "Pressure":
    val = st.number_input("Enter value in Pascals (Pa):", value=101325.0)
    col1, col2 = st.columns(2)
    col1.metric("Bar", val / 100000)
    col2.metric("PSI", round(val * 0.000145038, 3))

elif conversion_type == "Force":
    val = st.number_input("Enter value in Newtons (N):", value=1.0)
    col1, col2 = st.columns(2)
    col1.metric("Kilonewtons (kN)", val / 1000)
    col2.metric("Pound-force (lbf)", round(val * 0.224809, 3))

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.write("Developed for Mechanical Engineering Coursework")
