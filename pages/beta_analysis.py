import streamlit as st

st.header('Portfolio Performance & Beta Analysis')
container1 = st.container(border=True)
container1.slider('Risk-Free Rate (%)', max_value=10)

col1, col2 = st.columns(2, border=True)
with col1:
    st.metric('Sharpe Ratio (SR)', '1.381')

with col2:
    st.metric('Coefficient of Variation (CV)', '0.08%')

container2 = st.container(border=True)
container2.subheader('Beta Coefficient Calculator')
col3, col4 = container2.columns(2, border=True)

with col3:
    st.number_input('Covariance ')

with col4:
    st.number_input('Portfolio Variance')

container3 = st.container(border=True)
container3.metric('Beta (β)', '0.22')