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
investment_category = st.selectbox("Category", ["Taxable", "401k/403b", "457b", "IRA", "HSA", "Cryptocurrency", "Roth 401k/403b", "Roth 457b", "Roth IRA", "529 Plan"])
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
    new_dent = pd.DataFrame([[debt_description, debt_amount, investment_amount, interest_rate, minimum_payment]], columns=['Description', 'Amount', 'Interest Rate', 'Minimum Payment'])
    st.session_state.debts = pd.concat([st.session_state.investments, new_investment], ignore_index=True)

# Display the investments
st.write("Debts:")
st.dataframe(st.session_state.debts)

st.title("Fixed Income")

# Create an empty DataFrame for income
if 'income' not in st.session_state:
    st.session_state.income = pd.DataFrame(columns=['Type', 'Amount', 'Estimated Hours'])

# Input fields for income
income_type = st.selectbox("Income Type", ["Salary", "Hourly Wage"])
income_amount = st.number_input("Amount", min_value=0.0, format="%.2f", key='income_amount')
estimated_hours = st.number_input("Estimated Hours", min_value=0.0, format="%.2f")

# Add income button
if st.button("Add Fixed Income"):
    new_income = pd.DataFrame([[income_type, income_amount, estimated_hours]], columns=['Type', 'Amount', 'Estimated Hours'])
    st.session_state.income = pd.concat([st.session_state.income, new_income], ignore_index=True)

# Display the income
st.write("Income:")
st.dataframe(st.session_state.income)

st.title("Financial Goal")

# Create an empty DataFrame for goals
if 'goals' not in st.session_state:
    st.session_state.goals = pd.DataFrame(columns=['Description'])

financial_goal = st.text_input("Financial Goal")

# Add goal button
if st.button("Add Goal"):
    new_goal = pd.DataFrame([[financial_goal]], columns=['Description'])
    st.session_state.goals = pd.concat([st.session_state.goals, new_goal], ignore_index=True)

# Display the goals
st.write("Goals:")
st.dataframe(st.session_state.goals)

if st.button("get llm response"):

    # create savings embedding query

    savings = []

    for index, row in st.session_state.savings.iterrows():
        # create an object for each savings
        saving = {
            "description": row['Description'],
            "amount": row['Amount']
        }

    assets = []

    for index, row in st.session_state.assets.iterrows():
        # create an object for each asset
        asset = {
            "description": row['Description'],
            "purchase_price": row['Purchase Price'],
            "current_value": row['Current Value'],
            "status": row['Status']
        }

    investments = []

    for index, row in st.session_state.investments.iterrows():
        # create an object for each investment
        investment = {
            "category": row['Category'],
            "description": row['Description'],
            "amount": row['Amount'],
            "growth_rate": row['Growth Rate'],
            "dividend_yield": row['Dividend Yield']
        }

    debts = []

    for index, row in st.session_state.debts.iterrows():
        # create an object for each debt
        debt = {
            "description": row['Description'],
            "amount": row['Amount'],
            "interest_rate": row['Interest Rate'],
            "minimum_payment": row['Minimum Payment']
        }

    income = []

    for index, row in st.session_state.income.iterrows():
        # create an object for each income
        income = {
            "type": row['Type'],
            "amount": row['Amount'],
            "estimated_hours": row['Estimated Hours']
        }

    goals = []

    for index, row in st.session_state.goals.iterrows():
        # create an object for each goal
        goal = {
            "description": row['Description']
        }


    # create assets embedding query