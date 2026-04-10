import streamlit as st
import math


st.header('Porfolio & Risk Simulator ')
st.divider()

def update_b():
    st.session_state.w_b = 100 - st.session_state.w_a_slider
    st.session_state.update({'w_a': st.session_state.w_a_slider})

def sync_state(key):
    st.session_state[key] = st.session_state[f'{key}_slider']






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
    container.subheader('Two-asset portfolio construction')
    container.divider()

    st.slider('**Asset A weight (ωA)**', value= st.session_state.w_a, 
              key= 'w_a_slider', on_change= update_b)
    
    weight_a = st.session_state.w_a
    weight_b = st.session_state.w_b

    st.info(f'**Asset B weight (ωB) is automatically set to: {weight_b}**')

    #st.slider('Asset B weight (ωB)', value= st.session_state.w_b, key= 'w_b_slider', on_change= update_a)
    
    st.slider('**Correlation**', value= st.session_state.corr, 
              min_value=-1.0,
               max_value=1.0, step=0.1,
               on_change= sync_state, args=('corr',),
               key= 'corr_slider')

    corra_b = st.session_state.corr
    

with col2:
    
        st.number_input('**Volatility (σA)**', value = st.session_state.vol_a,
                        key= 'vol_a_slider',
                        on_change= sync_state, args=('vol_a',))
        
        st.number_input('**Return (rA)**',value = st.session_state.r_a,
                        key= 'r_a_slider',
                        on_change= sync_state, args=('r_a',))
        
        vol_a = st.session_state.vol_a
        return_a = st.session_state.r_a
        

    
        st.number_input('**Return (rB)**', value = st.session_state.r_b,
                        key= 'r_b_slider',
                        on_change= sync_state, args=('r_b',))
        
        st.number_input('**Volatility (σB)**', value = st.session_state.vol_b,
                        key= 'vol_b_slider',
                        on_change= sync_state, args=('vol_b',))
        
        return_b = st.session_state.r_b
        vol_b = st.session_state.vol_b
        

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
    st.metric('**Expected Return (rP)**', f'{p_return: .2f}%')

with col6:
    st.metric('**Portfolio Volatility (σ)**', f'{volatility: .2f}%')

with col7:
    st.metric('**Interaction Risk Removed**', f'{risk_saved: .2f}%')

container = st.container(border=True)
container.metric('**Risk Gap**', f'{variance_red:.2f}')
    
if corra_b < 0:
    st.info("**Negative correlation creates a hedge, allowing assets to cancel out each other's risks**")






st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")