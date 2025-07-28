import streamlit as st
import math

# ----- FUNCTIONS -----
def calculate_factorial(n):
    if n < 0:
        return "❌ Factorial not defined for negative numbers"
    return math.factorial(n)

def calculate_power(base, exponent):
    return math.pow(base, exponent)

def calculate_square_root(n):
    if n < 0:
        return "❌ Square root not defined for negative numbers"
    return math.sqrt(n)

# ----- STREAMLIT UI -----
st.title("🧮 Math Function Calculator")
st.write("Choose a function to calculate:")

option = st.selectbox("Select Operation", ["Factorial", "Power", "Square Root"])

if option == "Factorial":
    num = st.number_input("Enter a non-negative integer", min_value=0, step=1, format="%d")
    if st.button("Calculate Factorial"):
        result = calculate_factorial(num)
        st.success(f"Factorial of {num} = {result}")

elif option == "Power":
    base = st.number_input("Enter base", value=2.0)
    exponent = st.number_input("Enter exponent", value=3.0)
    if st.button("Calculate Power"):
        result = calculate_power(base, exponent)
        st.success(f"{base} ^ {exponent} = {result}")

elif option == "Square Root":
    num = st.number_input("Enter a number", value=0.0)
    if st.button("Calculate Square Root"):
        result = calculate_square_root(num)
        st.success(f"Square root of {num} = {result}")
