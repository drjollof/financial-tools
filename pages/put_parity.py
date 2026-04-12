import math
import streamlit as st

def calculate_arb(stock_price , strike_price, risk_free, call_price, time, put_price):
    r = risk_free/100
    T = time/365
    PV = strike_price * math.exp(-r * T)

    F_C = call_price + PV 
    P_C = put_price + stock_price
    gap = abs(F_C - P_C)





    return F_C, P_C, gap


st.title('**Put-Call Parity (Arbitrage Detector)**')

st.markdown("""
*Detect market mispricing by applying the law of equilibrium between identical portfolios. 
Compare the Fiduciary Call and Protective Put to identify arbitrage alerts when assets are incorrectly priced relative to the risk-free rate*
""")

st.divider()

col1, col2 = st.columns(2, border= True)

with col1:
    st.subheader('Market Data')
    stock_p = st.number_input('**Stock Price ($)**')
    t = st.number_input('**Time to Expiry (days)**', max_value=1460)
    rf = st.slider('**Risk Free Rate (%)**')
    

with col2:
    st.subheader('Option Data')
    c_p = st.number_input('**Call Price ($)**')
    p_p = st.number_input('**Put Price ($)**')
    strike_p = st.number_input('**Strike Price ($)**')

container = st.container(border=True)

F_C , P_C, gap = calculate_arb(stock_p, strike_p,rf,c_p, t, p_p)

if round(F_C, 2) > round(P_C, 2):
    container.error('**Arbitrage Detected!**  \nBuy Protective Put and Sell Fiduciary Call')
elif round(F_C, 2) < round(P_C, 2) :
    container.error('**Arbitrage Detected!**  \nBuy Fiduciary Call and Sell Protective Put')

else:    
    container.success('**No Arbitrage Detected!**')
 
st.divider()
col3, col4, col5 = st.columns(3, border=True)

with col3:
    st.metric('**Fiduciary Call Cost**', f'${F_C:.2f}')

with col4:
    st.metric('**Protective Put Cost**', f'${P_C:.2f}')

with col5:
    st.metric('**Arbitrage Gap**', f'${gap:.2f}')







st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")