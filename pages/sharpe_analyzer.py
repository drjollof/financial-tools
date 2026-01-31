import streamlit as st

st.header('Risk-Adjusted Performance (Sharpe Ratio)')
st.divider()

st.slider('Risk-Free Rate (%)',max_value=10)


col1 , col2 = st.columns(2, border=True)
with col1: 
    st.number_input('Asset Return (%)')

with col2:
    st.number_input('Annual Volatility (%)')


st.divider()
container = st.container(border= True, horizontal= True, 
                         horizontal_alignment="center")

container.metric(
        label="SHARPE RATIO",
        value="0.33",
        )




