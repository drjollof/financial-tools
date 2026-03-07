import streamlit as st

st.header('Equity Research')

col1, col2 = st.columns(2, border=True)

with col1:
    st.subheader('Fundamental Inputs')
    st.number_input('Stock Price ($)')
    st.number_input('Earnings Per Share (EPS)')
    st.number_input('Book Value ($)')
    st.slider('Growth Rate (%)')

with col2:
    st.subheader('Key Ratios & Analysis')
    col3, col4 = st.columns(2, border=True)
    with col3:
        st.metric('P/E Ratio', '15.0x')
    with col4:
        st.metric('P/B Ratio', '1.8x')
    
    container = st.container(border=True)
    container.metric('PEG Ratio', '0.75x')
    container.success('')