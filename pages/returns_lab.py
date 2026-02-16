import streamlit as st


st.header('Multi-Method Performance Tracker')
st.divider()

col1, col2 = st.columns(2, border=False)
with col1:

 st.number_input('Initial Price($)')
 with col2:
    st.number_input('Final Price ($)')
 is_dividend = st.checkbox('Did the asset pay Dividends?')

if is_dividend:
 st.number_input('Total Dividend Amount ($)')
 
st.divider()

col3, col4, col5 = st.columns(3, border= True, width='stretch')
with col3:
  st.metric('Arithmetic Return (%)', '34')

with col4:
  st.metric('Logarithmic Return (%)', '15')
with col5:
  st.metric('Dividend Yield (%)', '5')