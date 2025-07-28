import streamlit as st
import phonenumbers
import pandas as pd

st.set_page_config(page_title="🌐 Phone Number Formatter", layout="centered")

st.title("🌐 International Phone Number Formatter")

st.markdown("Paste one or more phone numbers (comma, space, or newline separated):")

user_input = st.text_area("Phone Numbers", height=200, placeholder="+14155552671, 9876543210, 00442079460123")

format_type = st.selectbox("Select Format", ["International (+XX)", "National", "E.164", "Raw Digits"])

default_country = st.text_input("Default Country (for numbers without country code)", value="IN").strip().upper()

# --- Utility Functions ---

def extract_numbers(text):
    """Splits input string into clean list of phone number strings."""
    separators = [',', '\n', '\t', ' ']
    for sep in separators:
        text = text.replace(sep, '\n')
    return [line.strip() for line in text.strip().splitlines() if line.strip()]

def format_number(number, fmt, default_region="IN"):
    try:
        # Normalize "0044..." → "+44..."
        number = number.strip()
        if number.startswith("00"):
            number = "+" + number[2:]

        # Parse with or without region
        if number.startswith("+"):
            parsed = phonenumbers.parse(number, None)
        else:
            parsed = phonenumbers.parse(number, default_region)

        if not phonenumbers.is_valid_number(parsed):
            return "❌ Invalid"

        # Formatting styles
        if fmt == "International (+XX)":
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        elif fmt == "National":
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        elif fmt == "E.164":
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        elif fmt == "Raw Digits":
            return str(parsed.national_number)
        else:
            return "⚠️ Unknown Format"
    except Exception:
        return "❌ Error"

# --- Main Logic ---

if st.button("Format Numbers"):
    numbers = extract_numbers(user_input)
    results = [format_number(num, format_type, default_region=default_country) for num in numbers]

    df = pd.DataFrame({
        "Original": numbers,
        "Formatted": results
    })

    st.success(f"✅ Processed {len(df)} numbers.")
    st.dataframe(df, use_container_width=True)

    # Download CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Results as CSV", data=csv, file_name="formatted_phone_numbers.csv", mime="text/csv")
