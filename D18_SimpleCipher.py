import streamlit as st

# Title
st.title("🔤 Letter Shifter (Shift +1 in Alphabet)")

# Input from user
text = st.text_input("Enter a word or sentence:")

# Shift function
def shift_text(s):
    result = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            result += char  # keep non-letters as is
    return result

# Button to perform shift
if st.button("Shift Letters"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        shifted = shift_text(text)
        st.success(f"🔁 Shifted Text: **{shifted}**")
