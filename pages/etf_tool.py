import streamlit as st

st.header('ETF Net Asset Value (NAV) Calculator')
container = st.container(border=True)
col1, col2, col3 = container.columns(3, border=True)

with col1:
    st.number_input('Total Assets')
with col2:
    st.number_input('Liabilities')

with col3:
    st.number_input('Shares Outstanding')

container2 = st.container(border=True)
col4, col5, col6 = container2.columns(3)

with col5:
    st.metric('NAV per Share ($)', '$1.768')