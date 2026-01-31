import streamlit as st


def real_return(nominal, inflation):
        rr = nominal - inflation
        return rr

st.header('Inflation & Real Returns')
st.divider()

col1 , col2 = st.columns(2, border= True)

with col1:
    nir = st.slider('Nominal Interest Rate(%)')
    ir = st.slider('Inflation Rate(%)', )
    rr = real_return(nir, ir)
   

with col2:
    st.metric(label='Real Return:', value = f'{rr}%')
    if rr > 0:
        st.info('Your purchasing Power is increasing')
    else: 
        st.warning('Your purchasing power is decreasing')
