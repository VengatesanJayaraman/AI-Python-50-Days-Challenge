import streamlit as st

# App title
st.title("🔢 Sum of Numbers from 1 to N")

# Input: Get the number N
n = st.number_input("Enter a positive integer (N)", min_value=1, step=1)

# Button to trigger calculation
if st.button("Calculate Sum"):
    total = 0
    for i in range(1, int(n) + 1):
        total += i
    st.success(f"The sum of numbers from 1 to {int(n)} is: **{total}**")
