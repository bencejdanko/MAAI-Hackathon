import streamlit as st
import pandas as pd

st.title("Savings")

# Create an empty DataFrame for savings
if 'savings' not in st.session_state:
    st.session_state.savings = pd.DataFrame(columns=['Description', 'Amount'])

# Input fields for savings
description = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

# Add savings button
if st.button("Add Savings"):
    new_saving = pd.DataFrame([[description, amount]], columns=['Description', 'Amount'])
    st.session_state.savings = pd.concat([st.session_state.savings, new_saving], ignore_index=True)

# Display the savings
st.write("Savings:")
st.dataframe(st.session_state.savings)

st.title("Assets")

# Create an empty DataFrame for assets
if 'assets' not in st.session_state:
    st.session_state.assets = pd.DataFrame(columns=['Description', 'Purchase Price', 'Current Value', 'Status'])

# Input fields for assets
asset_description = st.text_input("Asset Description")
purchase_price = st.number_input("Purchase Price", min_value=0.0, format="%.2f")
current_value = st.number_input("Current Value", min_value=0.0, format="%.2f")
status = st.selectbox("Status", ["Fully Owned", "Leased"])

# Add asset button
if st.button("Add Asset"):
    new_asset = pd.DataFrame([[asset_description, purchase_price, current_value, status]], columns=['Description', 'Purchase Price', 'Current Value', 'Status'])
    st.session_state.assets = pd.concat([st.session_state.assets, new_asset], ignore_index=True)

# Display the assets
st.write("Assets:")
st.dataframe(st.session_state.assets)

