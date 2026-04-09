import streamlit as st

def get_metrics(asset_return, volatility, risk_free):
    if volatility > 0:
        premium = asset_return - risk_free
        sharpe = premium / volatility
        
    else:
        premium = asset_return - risk_free
        sharpe = 0
    return sharpe , premium


st.header('Risk-Adjusted Performance (Sharpe Ratio)')
st.divider()

container0 = st.container(border=True)

rf = container0.slider('**Risk-Free Rate (%)**',
                      max_value=10,
                      help="The return on a safe investment, like a Treasury Bill")


col1 , col2 = st.columns(2, border=True)
with col1: 
    rp = st.number_input('**Expected Asset Return (%)**',
                                   value= 4,
                                   help="The total return you expect from the risky asset.")

with col2:
    sigma = st.number_input('**Asset Volatility (%)**',
                                        value= 5,
                                        help="The standard deviation of returns. This represents the 'stress' or price swings of the investment.")


sharpe_ratio , premium = get_metrics(rp, sigma, rf)

previous_ratio = sharpe_ratio

st.divider()

container = st.container(border= True, horizontal= True, 
                         horizontal_alignment="center")

col3, col4 = container.columns(2, border=True)

with col3:
    st.metric('**MARKET PREMIUM**',
              value=f'{premium:.2f}%',
              help="This is the excess return earned specifically for taking the risk."
              )




with col4:
    st.metric(
        label="**SHARPE RATIO**",
        value=f'{sharpe_ratio}',
        help="This is the investment's return relative to its risk"
        )
    

container2 = st.container(border=True)

if sharpe_ratio >= 1.0 and sigma > 0:
    container2.success(" **You are getting high returns relative to the risk**")

elif sharpe_ratio > 0 and sigma > 0:
    
    container2.warning(" **You are being compensated for the risk, but there may be more efficient options** ")

elif sharpe_ratio < 0 and sigma > 0:
   
    container2.error(" **Your return is lower than the risk-free rate. You are taking risk for no extra reward** ")


elif sigma == 0:
    container2.error(' **Volatitility is currently at 0. This indicates little to no risk on investment** ')

else:
    container2.info(" **You are not earning anything above what you could have made from a 'safe' investment** ")

    