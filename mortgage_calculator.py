#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import numpy as np

def calculate_monthly_payment(principal, annual_interest_rate, years):
    # Convert annual interest rate from percent to decimal and monthly
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # Total number of payments
    total_payments = years * 12
    # Calculate monthly payment
    monthly_payment = principal * (monthly_interest_rate * np.power(1 + monthly_interest_rate, total_payments)) / (np.power(1 + monthly_interest_rate, total_payments) - 1)
    return monthly_payment

# Title of the app
st.title('Mortgage Calculator')

# Mortgage inputs
principal = st.number_input('Loan Amount (Principal)', min_value=1000, max_value=1000000, value=100000)
annual_interest_rate = st.number_input('Annual Interest Rate (%)', min_value=0.1, max_value=20.0, value=3.5)
years = st.number_input('Loan Term (Years)', min_value=1, max_value=30, value=20)

# Calculate button
if st.button('Calculate Monthly Payment'):
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    st.write(f'Monthly Payment: ${monthly_payment:.2f}')
    
# streamlit run C:\Users\brian\anaconda3\Lib\site-packages\ipykernel_launcher.py


# In[ ]:




