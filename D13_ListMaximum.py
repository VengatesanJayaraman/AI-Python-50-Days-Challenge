import streamlit as st

# App title
st.title("📊 Number Analysis Tool")

# Input from user
input_str = st.text_input("Enter numbers separated by commas (e.g., 45, 12, 89, 3, 67):")

if st.button("Analyze"):
    try:
        # Convert input to list of integers
        num_list = [int(x.strip()) for x in input_str.split(",")]

        # Find largest and smallest manually
        largest = num_list[0]
        smallest = num_list[0]

        for num in num_list[1:]:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num

        sorted_list = sorted(num_list)

        # Display results
        st.success(f"✅ Largest number: **{largest}**")
        st.success(f"✅ Smallest number: **{smallest}**")
        st.info(f"🔢 Sorted list: {sorted_list}")

    except ValueError:
        st.error("❌ Please enter a valid list of numbers separated by commas.")
