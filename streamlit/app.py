import streamlit as st
import pandas as pd

# Title of the app
st.title("Expense Tracker")

# Create an empty DataFrame
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

# Input fields
date = st.date_input("Date")
description = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0, format="%.2f")

# Add expense button
if st.button("Add Expense"):
    new_expense = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

# Display the expenses
st.write("Expenses:")
st.dataframe(st.session_state.expenses)