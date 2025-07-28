import streamlit as st

# ---------- Functions ----------
def capitalize_text(text):
    return text.upper()

def reverse_text(text):
    return text[::-1]

def count_characters(text):
    return len(text)

# ---------- Streamlit App ----------
st.title("🔤 Text Utility App")

# User input
user_input = st.text_input("Enter your text:")

if user_input:
    st.subheader("🛠️ Results")

    st.write("**🔠 Capitalized:**", capitalize_text(user_input))
    st.write("**🔁 Reversed:**", reverse_text(user_input))
    st.write("**🔢 Character Count:**", count_characters(user_input))
