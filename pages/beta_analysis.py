import streamlit as st

st.header('Portfolio Performance & Beta Analysis')
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
    else:
        sharpe = (p_return - rf)/p_volatility
        cv = p_volatility/port_return
    return sharpe , cv

def calc_beta(new_vol, p_vol, new_corr, p_var):
    covariance = new_corr * new_vol * p_vol
    if p_var == 0:
        beta = 0
    else:
        beta = covariance/p_var
    return beta


risk_free = container1.slider('Risk-Free Rate (%)', max_value=10)


sharpe , coef_v = calc_metrics(port_return, risk_free, port_vol)
col1, col2 = st.columns(2, border=True)
with col1:
    st.metric('Sharpe Ratio (SR)', f'{sharpe:.2f}')

with col2:
    st.metric('Coefficient of Variation (CV)', f'{coef_v:.2f}')

container2 = st.container(border=True)
container2.subheader('Beta Coefficient Calculator')
col3, col4 = container2.columns(2, border=True)

with col3:
    asset_vol = st.number_input('New Asset Volatility')
    asset_corr = st.slider('New Asset Correlation', min_value =-1.0 ,max_value= 1.0, step=0.1)
    

with col4:
    st.metric('Portfolio Volatility', f'{port_vol:.2f}')
   
beta = calc_beta(asset_vol, port_vol, asset_corr, port_var)
container3 = st.container(border=True)
container3.metric('Beta (β)', f'{beta: .2f}')
