import streamlit as st

# App title
st.title("📝 Name Length Checker")

st.write("Enter 5 names below:")

# Input fields for 5 names
name1 = st.text_input("Name 1")
name2 = st.text_input("Name 2")
name3 = st.text_input("Name 3")
name4 = st.text_input("Name 4")
name5 = st.text_input("Name 5")

# Button to display names and lengths
if st.button("Show Names and Lengths"):
    names = [name1, name2, name3, name4, name5]
    
    # Filter out any empty entries
    non_empty_names = [name for name in names if name.strip()]
    
    if len(non_empty_names) < 5:
        st.warning("⚠️ Please enter all 5 names.")
    else:
        st.subheader("📋 Name List with Lengths:")
        for name in non_empty_names:
            st.write(f"🔹 **{name}** – {len(name)} characters")
