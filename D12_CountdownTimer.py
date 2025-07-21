import streamlit as st
import time

# App title
st.title("⏳ Countdown Timer")

# Start countdown on button click
if st.button("Start Countdown"):
    countdown = st.empty()  # placeholder for dynamic text

    for i in range(10, -1, -1):
        countdown.markdown(f"### ⏰ {i} seconds remaining")
        time.sleep(1)  # wait for 1 second

    countdown.markdown("## 🎉 Time's up!")
