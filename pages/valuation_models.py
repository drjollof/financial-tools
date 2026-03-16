import streamlit as st

st.header('Intrinsic Value Calculator ')



st.markdown("""
*Determine the fair value of a stock based on dividend growth expectations.
             Use GGM for stable companies and the H-Model for firms transitioning from high growth to maturity.*
""")



st.divider()

st.subheader('Gordon Growth Model',
             help='GGM assumes constant growth.')

col1, col2 , col3 = st.columns(3, border=True)

with col1:
    d1 = st.number_input("**Expected Next Dividend ($D_1$)**",
                            value=2, 
                            help='The dividend expected to be paid in the next year.')
    
with col2:
    k = st.number_input('**Required Rate of Return ($k$) %**', 
                        value=10.0,
                        help="The investor's required return (Cost of Equity).") / 100

with col3:
    g = st.number_input('**Constant Growth Rate ($g$) %**',  
                        value=5.0,  
                        help='The rate at which dividends are expected to grow indefinitely.') / 100


container = st.container(border=True)
if g >= k:
        
        st.error('The growth rate ($g$) must be strictly less than the required return ($k$).')
        intrinsic_value = 0.0

else:
        intrinsic_value = d1 / (k - g)
        
        container.success(f"### Intrinsic Value: ${intrinsic_value:.2f}")

st.write('')

st.subheader('H-Model',
             help= 'H-Model assumes high growth that slows linearly over time')

col3, col4 = st.columns(2, border=True)

with col3:
    d0 = st.number_input('**Current Dividend ($D_0$)**', 
                         min_value=0.01, 
                         value=2.0, 
                         step=0.1, 
                         help='The most recent dividend paid.')
    
    gs = st.number_input('**Short-term (High) Growth ($g_s$) %**', 
                         min_value=0.0, 
                         value=12.0, 
                         step=0.5, 
                         help='The initial high growth rate.') / 100
    
    gn = st.number_input('**Terminal (Normal) Growth ($g_n$) %**',
                          value=5.0, 
                          help='The steady-state growth rate after the transition.') / 100
    

with col4:
    k_h = st.number_input('**Required Rate of Return ($k$) %**',
                            value=10.0, 
                            help="The investor's required return.") / 100
    

    years = st.number_input('**Years of High Growth**', 
                            value=10, 
                            help='Total time for growth to drop from high to normal.')
    h = years / 2  

container = st.container(border=True)

if gn >= k_h:
    container.error('The terminal growth rate ($g_n$) must be strictly less than the required return ($k$).')
    intrinsic_value = 0.0

else:
        term1 = d0 * (1 + gn)
        term2 = d0 * h * (gs - gn)
        intrinsic_value = (term1 + term2) / (k_h - gn)
        
        container.success(f"### Intrinsic Value: ${intrinsic_value:.2f}")


