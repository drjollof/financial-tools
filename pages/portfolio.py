import streamlit as st
import math


st.header('Porfolio Simulator & Risk Analysis')


def portfolio(w1,w2,v1,v2,r1,r2,corr):
    w1 = w1/100
    w2 = w2/100
    p_variance = (w1**2) * (v1**2) + (w2**2) * (v2**2) + 2*(corr*w1*w2*v1*v2)
    p_volatility = math.sqrt(p_variance)
    portfolio_return = w1*r1 + w2*r2
    variance_red = (1-corr) * (2*(w1*w2*v1*v2))
    interaction_risk = 2*(corr*w1*w2*v1*v2)
    return p_variance, p_volatility, variance_red, portfolio_return, interaction_risk





col1, col2 = st.columns(2, border=True)

with col1:
    container = st.container(border=False)
    container.text('Two-asset portfolio construction')
    weight_a = st.slider('Asset A weight (ωA)')
    weight_b = st.slider('Asset B weight (ωB)', value= 100 - weight_a)
    corra_b = st.slider('Correlation',min_value=-1.0, max_value=1.0, step=0.1)

with col2:
    col3, col4 = st.columns(2)
    with col3:
        return_a = st.number_input('Return (Ra)')
        vol_a = st.number_input('Volatility (σA)')

    with col4:
        return_b = st.number_input('Return (B)')
        vol_b = st.number_input('Volatility (σB)')

st.divider()

variance, volatility, variance_red, p_return, int_risk = portfolio(weight_a,weight_b,
                                                         vol_a,vol_b,
                                                         return_a,return_b,
                                                         corra_b)

risk_saved = (1 - corra_b) * 100
st.session_state['port_vol'] = volatility
st.session_state['port_return'] = p_return
st.session_state['port_var'] = variance

   

col5,col6,col7 = st.columns(3, border=True)
with col5:
    st.metric('Expected Return (Rp)', f'{p_return: .2f}%')

with col6:
    st.metric('Portfolio Volatility (σ)', f'{volatility: .2f}%')

with col7:
    st.metric('Interaction Risk Removed', f'{risk_saved: .2f}%')
    st.metric('Risk Gap', f'{variance_red:.2f}')
    
if corra_b < 0:
    st.info("Negative correlation creates a hedge, allowing assets to cancel out each other's risks")

