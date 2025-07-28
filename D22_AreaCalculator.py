import streamlit as st
import math

# ----- Calculator Functions -----

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# ----- Streamlit UI -----

st.set_page_config(page_title="Area Calculator", layout="centered")
st.title("📐 Area Calculator")

shape = st.selectbox("Select Shape", ["Circle", "Rectangle", "Triangle"])

if shape == "Circle":
    radius = st.number_input("Enter Radius (cm)", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_circle(radius)
        st.success(f"Area of Circle: {area:.2f} cm²")

elif shape == "Rectangle":
    length = st.number_input("Enter Length (cm)", min_value=0.0, format="%.2f")
    width = st.number_input("Enter Width (cm)", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_rectangle(length, width)
        st.success(f"Area of Rectangle: {area:.2f} cm²")

elif shape == "Triangle":
    base = st.number_input("Enter Base (cm)", min_value=0.0, format="%.2f")
    height = st.number_input("Enter Height (cm)", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_triangle(base, height)
        st.success(f"Area of Triangle: {area:.2f} cm²")
