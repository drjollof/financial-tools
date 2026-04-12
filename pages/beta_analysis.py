import streamlit as st

st.title('Portfolio Performance')

st.markdown("""
*Audit the custom portfolio's efficiency using risk-adjusted metrics. Evaluate return-to-risk payoff through the Sharpe Ratio and CV, and assess maximum expected downside using Value at Risk (VaR).*
""")

st.divider()

port_vol = st.session_state['port_vol']
port_return = st.session_state['port_return']
port_var = st.session_state['port_var']


if port_vol == 0 or port_return == 0:
    st.error('Portfolio volatility and return are not set, visit porfolio simulator  page to set portfolio parameters')

container1 = st.container(border=True)

def calc_metrics(p_return, rf, p_volatility):
    if p_volatility == 0 or port_return == 0:
        sharpe = 0
        cv = 0
        VaR = 0
    else:
        sharpe = (p_return - rf)/p_volatility
        cv = p_volatility/port_return
        VaR = p_return - (1.645 * p_volatility)
    return sharpe , cv , VaR




risk_free = container1.slider('**Risk-Free Rate (%)**',min_value= 0.0, max_value=10.0, step= 0.1)


sharpe , coef_v , VaR = calc_metrics(port_return, risk_free, port_vol)
col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.metric('**Sharpe Ratio (SR)**', f'{sharpe:.2f}')


with col2:
    st.metric('**Coefficient of Variation (CV)**', f'{coef_v:.2f}')

with col3:
    st.metric('**Value at Risk (VaR)**', f'{VaR:.2f}%')
    st.text('at 95% Confidence', )

container2 = st.container(border=True)
container2.subheader('Portfolio Metrics Interpretation')

col3, col4 , col5 = container2.columns(3, border=True)

with col3:
    if sharpe < 1.0:
        st.write('**Sharpe Ratio: Sub-optimal**')
        st.error('Your portfolio is underperforming relative to its risk. Consider lowering the correlation to increase risk gap and boost efficiency')
    
    elif sharpe > 1.0 and sharpe < 2.0:
        st.write('**Sharpe Ratio: Adequate**')
        st.info('You are receiving a solid return for the risk taken. This is a balanced portfolio')

    else:
        st.write('**Sharpe Ratio: Efficient**')
        st.success('Excellent Diversification! \n Your interaction risk removed is significantly protecting your returns. This is highly efficient')



with col4:
    
    if coef_v < 1.0:
        st.write('**Coefficient of Variation: Efficient**')
        st.success('You are taking less than 1 unit of risk for every 1% return. This is a sign of a well diversified portfolio')
    else:
        st.write('**Coefficient of Variation: High Risk-Cost**')
        st.error('You are paying more than 1 unit of risk for every 1% of return . Check if one of your assets has a very high volatility that is dragging down the efficiency')
        

with col5:

    if VaR >= 0:
        st.info('Unusually high safety: Worst-case scenario is still a gain')

    elif VaR > -10:
        st.write('**Value at Risk: Conservative**')
        st.success('Your pain threshold is low. Your losses are expected to be contained in a disaster. This is suitable for risk-averse investors')
    
    elif VaR > -20:
        st.write('**Value at Risk: Moderate**')
        st.info('You have a standard market risk profile. Be prepared for a significant paper loss during a market correcton')
    
    else: 
        st.write('**Value at Risk: Aggressive**')
        st.error(f'High loss potential. There is a 5% chance you could lose more than {VaR:.2f}% in a single period. Ensure you have the stomach for this volatility!')




st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")