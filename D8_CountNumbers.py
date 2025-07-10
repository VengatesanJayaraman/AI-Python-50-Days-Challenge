import streamlit as st

def count_numbers(numbers):
    positive = negative = zero = 0
    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    return positive, negative, zero

# Streamlit UI
st.title("🔢 Number Counter")

st.write("Enter a list of numbers separated by commas (e.g., `1, -2, 0, 4, -5`)")

user_input = st.text_input("Enter numbers:")

if user_input:
    try:
        number_list = [float(x.strip()) for x in user_input.split(",")]
        pos, neg, zero = count_numbers(number_list)

        st.success("✅ Results:")
        st.write(f"**Positive numbers:** {pos}")
        st.write(f"**Negative numbers:** {neg}")
        st.write(f"**Zeros:** {zero}")
    except ValueError:
        st.error("Please enter a valid list of numbers separated by commas.")
