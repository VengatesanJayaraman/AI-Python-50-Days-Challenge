import streamlit as st
import re

# App title
st.title("📊 Paragraph Analyzer")

st.write("Paste or type your paragraph below to analyze word, sentence, and character counts:")

# User input
paragraph = st.text_area("Enter paragraph here:", height=200)

# Button to analyze
if st.button("Analyze Text"):
    if not paragraph.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        # Word count
        words = paragraph.split()
        word_count = len(words)

        # Sentence count using regex (naive split on ., !, ?)
        sentence_count = len(re.findall(r'[.!?]+', paragraph))

        # Character count (excluding spaces)
        char_count = len(paragraph.replace(" ", ""))

        # Display results
        st.subheader("📈 Text Statistics")
        st.write(f"📝 **Word Count:** {word_count}")
        st.write(f"📚 **Sentence Count:** {sentence_count}")
        st.write(f"🔠 **Character Count (no spaces):** {char_count}")
