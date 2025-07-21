import streamlit as st

# App title
st.title("📧 Email Username Extractor")

# Input field
email = st.text_input("Enter your email address:")

# Button to extract username
if st.button("Extract Username"):
    if "@" in email and email.count("@") == 1:
        username = email.split("@")[0]
        st.success(f"✅ Username: **{username}**")
    else:
        st.error("❌ Please enter a valid email address.")
