import streamlit as st

# App title
st.title("🔄 Reverse Each Word in a Sentence")

# Input sentence
sentence = st.text_input("Enter a sentence:")

# Button to reverse words
if st.button("Reverse Words"):
    if sentence.strip() == "":
        st.warning("⚠️ Please enter a sentence.")
    else:
        # Split the sentence into words and reverse each word
        reversed_words = [word[::-1] for word in sentence.split()]
        reversed_sentence = " ".join(reversed_words)

        # Display result
        st.success(f"🔁 Reversed words: **{reversed_sentence}**")
