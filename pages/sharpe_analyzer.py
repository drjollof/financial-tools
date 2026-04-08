import streamlit as st

def get_sharpe(asset_return, volatility, risk_free):
    if volatility > 0:
        sharpe = (asset_return - risk_free) / volatility
    else:
        sharpe = 0
    return sharpe

st.header('Risk-Adjusted Performance (Sharpe Ratio)')
st.divider()

risk_free = st.slider('**Risk-Free Rate (%)**',
                      max_value=10)


col1 , col2 = st.columns(2, border=True)
with col1: 
    asset_return = st.number_input('**Asset Return (%)**',
                                   value= 4)

with col2:
    annual_volatility = st.number_input('**Annual Volatility (%)**',
                                        value= 5)


sharpe_ratio = get_sharpe(asset_return, annual_volatility, risk_free)
st.divider()
container = st.container(border= True, horizontal= True, 
                         horizontal_alignment="center")

container.metric(
        label="**SHARPE RATIO**",
        value=f'{sharpe_ratio}',
        )




