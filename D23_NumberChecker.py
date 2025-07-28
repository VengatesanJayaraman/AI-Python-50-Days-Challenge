import streamlit as st

# --- Functions ---
def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# --- Streamlit UI ---
st.set_page_config(page_title="Number Checker", page_icon="🔢")

st.title("🔢 Number Checker")
st.write("Enter a number to check if it's **positive**, **even**, or **prime**.")

number = st.number_input("Enter a number", step=1)

if st.button("Check"):
    st.write(f"👉 You entered: **{number}**")

    if is_positive(number):
        st.success("✅ The number is Positive.")
    elif number == 0:
        st.info("ℹ️ The number is Zero.")
    else:
        st.error("❌ The number is Negative.")

    if is_even(number):
        st.success("✅ The number is Even.")
    else:
        st.warning("⚠️ The number is Odd.")

    if is_prime(int(number)):
        st.success("✅ The number is Prime.")
    else:
        st.info("ℹ️ The number is Not Prime.")
