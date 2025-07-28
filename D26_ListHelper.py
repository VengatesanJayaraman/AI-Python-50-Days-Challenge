import streamlit as st

def calculate_max(numbers):
    return max(numbers) if numbers else None

def calculate_min(numbers):
    return min(numbers) if numbers else None

def calculate_sum(numbers):
    return sum(numbers) if numbers else 0

def calculate_avg(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    st.title("🔢 List Operations: Max, Min, Sum, Average")

    user_input = st.text_input("Enter a list of numbers separated by commas:", "10, 20, 30, 40, 50")

    try:
        numbers = [float(x.strip()) for x in user_input.split(",") if x.strip() != ""]

        st.write("✅ **List Entered:**", numbers)
        
        st.write("📌 **Maximum:**", calculate_max(numbers))
        st.write("📌 **Minimum:**", calculate_min(numbers))
        st.write("📌 **Sum:**", calculate_sum(numbers))
        st.write("📌 **Average:**", round(calculate_avg(numbers), 2))
        
    except ValueError:
        st.error("❌ Please enter only numbers separated by commas.")

if __name__ == "__main__":
    main()
