import streamlit as st

# App Title
st.set_page_config(page_title="Number Comparator", page_icon="🔢", layout="centered")
st.title("🔢 Number Comparison Tool")
st.markdown("Compare two numbers and find out which one is larger, smaller, or if they're equal.")

# Styled Input Section
with st.container():
    st.subheader("Enter Two Numbers to Compare")
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("🔹 First Number", format="%.2f", step=1.0)
    with col2:
        num2 = st.number_input("🔸 Second Number", format="%.2f", step=1.0)

# Compare Button
if st.button("🔍 Compare Now"):
    st.divider()
    st.subheader("🧠 Result")

    if num1 > num2:
        st.success(f"✅ The first number **({num1})** is **larger** than the second number **({num2})**.")
    elif num1 < num2:
        st.info(f"ℹ️ The second number **({num2})** is **larger** than the first number **({num1})**.")
    else:
        st.warning(f"⚖️ Both numbers are **equal** (**{num1} = {num2}**)")

# Footer Style
st.markdown("---")
st.markdown(
    "<center><small>Made with ❤️ using Streamlit</small></center>",
    unsafe_allow_html=True
)
