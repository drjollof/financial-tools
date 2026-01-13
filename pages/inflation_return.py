import streamlit as st


def real_return(nominal, inflation):
        rr = nominal - inflation
        return rr

st.header('Inflation & Real Returns')
st.divider()

col1 , col2 = st.columns(2, border= True)

with col1:
    nir = st.number_input('Nominal Interest Rate(%)', format = '%.1f' )
    ir = st.number_input('Inflation Rate(%)', format= '%.1f')
    rr = real_return(nir, ir)
   

with col2:
    st.metric(label='Real Return:', value = f'{rr}%')
    if rr > 0:
        st.info('Purchasing Power is increasing')
    else: 
        st.warning('Purchasing power is decreasing')
