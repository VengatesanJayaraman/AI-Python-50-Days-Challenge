import streamlit as st

st.title("Total Cost Calculator with Tax")

# Item Inputs
st.header("Enter Prices for 3 Items:")
item1 = st.number_input("Price of Item 1", min_value=0.0, format="%.2f")
item2 = st.number_input("Price of Item 2", min_value=0.0, format="%.2f")
item3 = st.number_input("Price of Item 3", min_value=0.0, format="%.2f")

# Tax selection
st.header("Select Tax Percentage")
tax_options = ["5%", "12%", "18%", "28%", "Custom"]
tax_choice = st.selectbox("Choose Tax Rate", tax_options)

if tax_choice == "Custom":
    custom_tax = st.number_input("Enter Custom Tax (%)", min_value=0.0, format="%.2f")
    tax_percent = custom_tax
else:
    tax_percent = float(tax_choice.strip('%'))

# Calculations
subtotal = item1 + item2 + item3
tax_amount = subtotal * (tax_percent / 100)
total_cost = subtotal + tax_amount

# Results
st.subheader("Summary")
st.write(f"Subtotal: ₹{subtotal:.2f}")
st.write(f"Tax @ {tax_percent}%: ₹{tax_amount:.2f}")
st.success(f"Total Cost (including tax): ₹{total_cost:.2f}")
