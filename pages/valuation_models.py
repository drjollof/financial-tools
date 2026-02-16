import streamlit as st

st.header('Intrinsic Value Calculator (Gordon Growth Model)')

col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.number_input('Expected Next Dividend (D1)')

with col2:
    st.number_input('Required Cost of Equity (%)')

with col3: 
    st.number_input('Constant Growth Rate (%)')

st.warning('Error: Growth (g) cannot be higher than or equal to cost of equity (k). This model is invalid')

st.divider()

container = st.container(border=True)
container.metric('Calculated Intrinsic Value (P0)', '5363')