import streamlit as st
import pandas as pd
import numpy as np

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

st.title("Investments")

# Create an empty DataFrame for investments
if 'investments' not in st.session_state:
    st.session_state.investments = pd.DataFrame(columns=['Category', 'Description', 'Amount', 'Growth Rate', 'Dividend Yield'])

# Input fields for investments
investment_category = st.selectbox("Category", ["US Stock Market", "US Mid Cap", "US Small Cap"])
investment_description = st.text_input("Investment Description")
investment_amount = st.number_input("Investment Amount", min_value=0.0, format="%.2f")
growth_rate = st.number_input("Growth Rate (%)", min_value=0.0, format="%.2f")
dividend_yield = st.number_input("Dividend Yield (%)", min_value=0.0, format="%.2f")

# Add investment button
if st.button("Add Investment"):
    new_investment = pd.DataFrame([[investment_category, investment_description, investment_amount, growth_rate, dividend_yield]], columns=['Category', 'Description', 'Amount', 'Growth Rate', 'Dividend Yield'])
    st.session_state.investments = pd.concat([st.session_state.investments, new_investment], ignore_index=True)

# Display the investments
st.write("Investments:")
st.dataframe(st.session_state.investments)

st.title("Debts")

# Create an empty DataFrame for investments
if 'debts' not in st.session_state:
    st.session_state.debts = pd.DataFrame(columns=['Description', 'Amount', 'Interest Rate', 'Minimum Payment'])

# Input fields for investments
debt_description = st.text_input("Debt Description")
debt_amount = st.number_input("Debt Amount", min_value=0.0, format="%.2f")
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, format="%.2f")
minimum_payment = st.number_input("Minimum Payment", min_value=0.0, format="%.2f")

# Add investment button
if st.button("Add Debt"):
    new_debt = pd.DataFrame([[debt_description, debt_amount, interest_rate, minimum_payment]], columns=['Description', 'Amount', 'Interest Rate', 'Minimum Payment'])
    st.session_state.debts = pd.concat([st.session_state.debts, new_debt], ignore_index=True)

# Display the investments
st.write("Debts:")
st.dataframe(st.session_state.debts)

st.title("Fixed Income")

# Create an empty DataFrame for income
if 'income' not in st.session_state:
    st.session_state.income = pd.DataFrame(columns=['Type', 'Amount'])

# Input fields for income
income_type = st.selectbox("Income Type", ["Cash", "Corporate Bonds", "10-year Treasury"])
income_amount = st.number_input("Amount", min_value=0.0, format="%.2f", key='income_amount')

# Add income button
if st.button("Add Fixed Income"):
    new_income = pd.DataFrame([[income_type, income_amount]], columns=['Type', 'Amount'])
    st.session_state.income = pd.concat([st.session_state.income, new_income], ignore_index=True)

# Display the income
st.write("Income:")
st.dataframe(st.session_state.income)

st.title('Investment Experience')

# Dropdown (selectbox) with options
investment_knowledge = st.selectbox(
    "How would you describe your experience in investing?",
    ("None", "Limited", "Good", "Extensive")
)

# Display the selected option
st.write(f'Selection: {investment_knowledge}')

st.title('Investment Goals')
investment_goal = st.selectbox("What's your primary investment goal?",
            ("None","Preserving my capital with minimal risk", \
            "Generating stable income", \
            "Achieving moderate growth while limiting risk", \
            "Maximizing long-term growth potential")
)
st.write(f'Selection: {investment_goal}')

st.title('Income Source')
income_source = st.selectbox("How stable is your current and future income?",
            ("None","Unstable", \
            "Somewhat Stable", \
            "Stable"))

st.write(f'Selection: {income_source}')

st.title('Investment Risk')
investment_risk = st.selectbox("On a scale of 10, what is your risk tolerance?",
            ("1 - Least Risk", "2", "3", "4", "5 - Medium Risk", "6",\
            "7", "8", "9", "10 - Most Risk"))

st.write(f'Selection: {investment_risk}')

import json

if st.button("get llm response"):


    # fetch from monte carlo

    # Combine all data into a single list of dictionaries
    combined_data = {
        "savings": st.session_state.savings.to_dict(orient='records'),
        "assets": st.session_state.assets.to_dict(orient='records'),
        "investments": st.session_state.investments.to_dict(orient='records'),
        "debts": st.session_state.debts.to_dict(orient='records'),
        "income": st.session_state.income.to_dict(orient='records'),
        "investment_knowledge": investment_knowledge,
        "investment_goal": investment_goal,
        "income_source": income_source,
        "investment_risk": investment_risk
    }
    combined_data_str = json.dumps(combined_data, indent=4)
    st.write("Combined Data:")
    st.text(combined_data_str)