import streamlit as st

# App title
st.title("👤 Full Name Formatter")

# Input field for full name
full_name = st.text_input("Enter your full name (First Middle Last):")

if st.button("Format Name"):
    # Split the name into parts
    name_parts = full_name.strip().split()

    if len(name_parts) < 2:
        st.error("❌ Please enter at least a first and last name.")
    else:
        first = name_parts[0]
        last = name_parts[-1]
        middle = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""

        # Display different formats
        st.subheader("🧾 Name Formats:")

        st.write(f"• First Last: **{first} {last}**")
        if middle:
            st.write(f"• First Middle Last: **{first} {middle} {last}**")
        st.write(f"• Last, First: **{last}, {first}**")
        if middle:
            st.write(f"• Last, First Middle: **{last}, {first} {middle}**")
        st.write(f"• Initials: **{''.join([p[0].upper() for p in name_parts])}**")
