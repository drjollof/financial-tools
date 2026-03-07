import streamlit as st


st.header('Credit Risk Calculator')

st.divider()

col1 , col2, col3 = st.columns(3, border=True)

with col1:
    st.number_input('Exposure at Default', value = 10000000)

with col2:
    st.slider('Probability of Default')

with col3:
    st.slider('Loss Given Default')

container = st.container(border=True,horizontal_alignment='center')
col4, col5 , col6 = container.columns(3, border=False)



with col5:
    st.metric('Expected Loss', '$20000',)

st.divider()

col7, col8 = st.columns(2, border=True)

with col7:
    st.slider('Corporate Bond Yield (%)')
    st.slider('Government Bond Yield (%)')

with col8:
    st.slider('Assumed Recovery Rate (%)')
    st.number_input('Credit Spread')

container2 = st.container(border=True)
col9, col10, co11 = container2.columns(3, border=False)

with col10:
    st.metric('Probability of Default', '8.33%')