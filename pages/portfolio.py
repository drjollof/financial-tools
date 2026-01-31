import streamlit as st

st.header('Porfolio Simulator & Risk Analysis')

col1, col2 = st.columns(2, border=True)

with col1:
    container = st.container(border=False)
    container.text('Two-asset portfolio construction')
    weight_a = st.slider('Asset A weight (ωA)')
    weight_b = st.slider('Asset B weight (ωB)', value= 100 - weight_a)
    corr = st.slider('Correlation',min_value=-1.0, max_value=1.0, step=0.1)

with col2:
    col3, col4 = st.columns(2)
    with col3:
        return_a = st.number_input('Return (Ra)')
        vol_a = st.number_input('Volatility (σA)')

    with col4:
        return_b = st.number_input('Return (B)')
        vol_b = st.number_input('Volatility (σB)')

st.divider()

col5,col6,col7 = st.columns(3, border=True)
with col5:
    st.metric('Expected Return (Rp)', '5.77%')

with col6:
    st.metric('Portfolio Volatility (σ)', '10.82%')

with col7:
    st.metric('Variance Reduction', '18.32%')