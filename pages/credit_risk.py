import streamlit as st
def calc_metrics(ead, pd, rr):
    lgd = 1 - (rr/100)
    loss = ead * pd/100 * lgd
    return lgd*100, loss

def calc_implied(ytm, rf, arr ):
    cs = ytm - rf
    lgd = 1 - (arr/100)
    ipd = cs/lgd
    return cs, ipd

st.header('Expected Loss Calculator' , 
          help='calculates the amount the bank expects to lose on a specific loan')
st.caption('Projected loss for specific bank loans.')

st.divider()

col1 , col2, col3 = st.columns(3, border=True)

with col1:
    ead = st.number_input('**Exposure at Default**', value = 10000000,
                    help='total amount the bank is owed at the time the borrower defaults')

with col2:
    pd = st.slider('**Probability of Default (%)**', value= 5,
              help='percentage chance the borrower will fail to repay')

with col3:
    rr = st.slider('**Recovery Rate (%)**', value=60)
    

container = st.container(border=True,horizontal_alignment='center')
col4, col5= container.columns(2, border=True)

lgd , loss = calc_metrics(ead, pd, rr)

with col5:
    st.metric('**Expected Loss**', f'${loss:,.0f}',
              help='average amount the bank should budget to lose on this loan')
with col4:
    st.metric('**Loss Given Default**', value = f'{lgd:.0f}%' , 
              help='portion of the loan the bank cannot recover' )

st.divider()

st.header('Implied Probability of Default', 
          help='calculates the chance of bankruptcy based on what public bond investors are charging at the moment')
st.caption('Default risk from from public bond spreads')



col7, col8 = st.columns(2, border=True)

with col7:
    ytm = st.slider('**Bond YTM (%)**',
              help="market rate for the company's bond")
    
    rf = st.slider('**Risk-Free Rate (%)**', 
              help='baseline interest rate of a safe investment e.g Treasury bond')

with col8:
    spread = st.number_input('**Credit Spread**', value= ytm - rf,
                    help='extra yield a risky bond pays over a risk-free goverment bond')
    
    arr = st.slider('**Assumed Recovery Rate (%)**', 
              help='how much investors expect to get back in bankruptcy')
    
container2 = st.container(border=True)
col9, col10, co11 = container2.columns(3, border=False)

cs, ipd = calc_implied(ytm, rf, arr)

with col10:
    st.metric('**Probability of Default**', f'{ipd:.2f}%', 
              help='CDS implied probability of default')
    




st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")