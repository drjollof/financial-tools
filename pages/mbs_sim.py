import streamlit as st

st.title('MBS Simulator')

col1, col2 = st.columns(2, border=True)

with col1:
    tps = st.number_input('Toal Pool Size ($M)', value= 300)
    tpl = st.slider('Total Pool Loss ($M)',min_value= 0, 
               max_value=tps,label_visibility='visible')
    
with col2:
    st.subheader('Tranche Par Values')
    s_t = st.number_input('Senior (A)', value=180)
    m_t = st.number_input('Mezzanine (B)', value= 70)
    e_t = st.number_input('Equity (C)', value= tps - (s_t + m_t) )

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

with col3:
    st.write('Equity (Tranche C)')
    st.write(f'STATUS:{c}')
    

with col4:
    st.write('Mezzanine (Tranche B)')
    st.write(f'STATUS:{b}')

with col5:
    st.write('Senior (Tranche A)')
    st.write(f'STATUS:{a}')