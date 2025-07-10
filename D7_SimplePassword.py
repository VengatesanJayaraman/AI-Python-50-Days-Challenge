import streamlit as st
import re

def is_password_valid(password, min_length=8):
    if len(password) < min_length:
        return False, f"Password must be at least {min_length} characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must include at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character."
    return True, "Password is strong."

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    valid, message = is_password_valid(password)
    if valid:
        st.success(message)
    else:
        st.error(message)
