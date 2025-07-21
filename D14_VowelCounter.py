import streamlit as st

# App title
st.title("🅰️ Vowel Counter")

# User input
text = st.text_input("Enter a word or sentence:")

# Vowel set
vowels = "aeiouAEIOU"

# Button to count vowels
if st.button("Count Vowels"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        st.success(f"✅ Number of vowels in the given text: **{count}**")
