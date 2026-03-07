import streamlit as st

def get_ratios(sp,eps,bv,gr):
    if eps > 0:
        P_E = sp / eps
    else:
         P_E = float('inf')

    if b_v > 0:
         
        P_B = sp / bv
    else:
         P_B = float('inf')

    if gr > 0 and eps > 0:
        PEG = P_E/gr

    else:
         PEG = float('inf')

    return P_E, P_B, PEG

st.header('Equity Research')

col1, col2 = st.columns(2, border=True)

with col1:
    s_p = st.number_input('**Stock Price ($)**', value=50)
    eps = st.number_input('**Earnings Per Share (EPS) ($)**', value=5, help='Net income generated for each outstanding share')
    
with col2:
    b_v = st.number_input('**Book Value ($)**', value=25, help="Company's net asset value for each outstanding share")
    g_r = st.slider('**Growth Rate (%)**', value=20, help='Expected annual growth rate')

    

pe , pb, peg = get_ratios(s_p, eps, b_v, g_r)
st.subheader('Key Ratios & Analysis')
col3, col4 = st.columns(2, border=True)
with col3:
        st.metric('**P/E Ratio**', f'{pe:.1f}x' if pe != float('inf') else 'N/A' ,
                  help='Price-to-Earnings')
        st.caption('Lower is generally better')
        
with col4:
        st.metric('**P/B Ratio**', f'{pb:.1f}x' if pb != float('inf') else 'N/A',
                  help='Compares market price to the accounting net asset value per share')
        st.caption('Values < 1 can indicate deep value')



    
container = st.container(border=True, horizontal=True)
container.metric('**PEG Ratio**', 
                 f'{peg:.2f}x', help='Adjusted P/E for the expected growth rate',
                 border=True)


if peg == float('inf'):
     container.error('Cannot compute PEG - invalid inputs')
elif peg < 1.0:
     container.success('**Potentially Undervalued** \n\n'
                'The stock appears cheap relative to its expected growth')
     
elif 1.0 <=  peg <= 1.3:
     container.warning('**Neutral / Fairly Valued** \n\n'
                'Price roughly matches expected growth')
else:
     container.error('**Potentially Overvalued** \n\n'
              'You are paying a high price relative to projected growth')