import streamlit as st

st.header('Mortgage-backed Security Waterfall Simulator')
st.divider()


st.subheader('Tranche Pool ($M)')
container1 = st.container(border=True)
tps = container1.number_input('**Total Pool Size ($M)**', value= 300)

st.subheader('Tranche Par Values ($M)')
col1, col2, col3 = st.columns(3, border=True)


with col1:
    
    s_t = st.number_input('**Senior (A)**', value=180)
    
    
    
with col2:
    m_t = st.number_input('**Mezzanine (B)**', value= 70)

with col3:
    e_t = st.number_input('**Equity (C)**', value= tps - (s_t + m_t) )

container2 = st.container(border=True)
tpl = container2.slider('**Total Pool Loss ($M)**',min_value= 0, 
               max_value=tps,label_visibility='visible')


def get_loss(total_loss, tranche_a, tranche_b, tranche_c):
    if tranche_c < total_loss:
        loss_c = tranche_c
        rem_loss = total_loss - loss_c

        if rem_loss < tranche_b:
            loss_b = rem_loss
            rem_loss = total_loss - (loss_c + loss_b )

            if rem_loss < tranche_a:
                loss_a = rem_loss

            else:
                loss_a = tranche_a

        else:
             loss_b = tranche_b
             loss_a = total_loss - (loss_c + loss_b)
             
             

    else:
        loss_c = total_loss 
        loss_b = 0
        loss_a = 0

    return loss_a, loss_b, loss_c
    
    
    

a, b , c = get_loss(tpl, s_t, m_t, e_t)

st.subheader('Tranche Status')

col3, col4, col5 = st.columns(3, border=True)

with col5:
    st.write('**Equity (Tranche C)**')

    if c == 0:
        st.success(f'**STATUS**: Protected \n \n **LOSS:** -${b}M')

    elif c >= e_t:
        st.error(f'**STATUS: Wiped Out** \n \n **LOSS:** -${c}M')

    else:
        st.warning(f'**STATUS**: Impaired \n \n **LOSS:** -${c}M')
    
    

with col4:
    st.write('**Mezzanine (Tranche B)**')

    if b == 0:
        st.success(f'**STATUS**: Protected \n \n **LOSS:** -${b}M')

    elif b >= m_t:
        st.error(f'**STATUS: Wiped Out** \n \n **LOSS:** -${b}M')

    else:
        st.warning(f'**STATUS**: Impaired \n \n **LOSS:** -${b}M')
    



with col3:
    st.write('**Senior (Tranche A)**')

    if a == 0:
        st.success(f'**STATUS**: Protected \n \n **LOSS:** -${a}M')

    elif a >= s_t:
        st.error(f'**STATUS: Wiped Out** \n \n **LOSS:** -${a}M')

    else:
        st.warning(f'**STATUS**: Impaired \n \n **LOSS:** -${a}M')
    





st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")