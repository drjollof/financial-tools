import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.header('Fractional Reserve Banking Simulator')
st.divider()

def bank_reserve(initial_deposit, RR: int):
    reserve = (RR/100) * initial_deposit
    lendable = initial_deposit - reserve
    return reserve, lendable




col1, col2 = st.columns(2,border=True)

with col1:
    initial_deposit = st.number_input('Initial Deposit($)')
    rr = st.slider('Reserve Ratio(%)')

    required_reserve , lendable = bank_reserve(initial_deposit, rr)


with col2:
    category = ['Required Reserves', 'Lendable Funds']
    values = [required_reserve, lendable]
    fig,ax = plt.subplots()
    if len(values) == 0 or np.nansum(values) == 0:
        st.warning("No valid data available to display the pie chart.")
    else:

        ax.pie(values, labels=category, autopct="%.0f%%")
        ax.axis('equal')

        st.pyplot(fig)