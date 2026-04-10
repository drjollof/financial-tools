import streamlit as st




def get_nav(assets, liabilities, shares):

    return (assets - liabilities) / shares



st.header('ETF Net Asset Value (NAV) Calculator')
container = st.container(border=True)

col1, col2 = container.columns(2, border=True)

with col1:
    assets = st.number_input('**Total Market Value of Assets ($)**',
                             value= 1000000,
                             help='The combined current market value of all securities (stocks, bonds, or cash) held in the ETF')

with col2:
    liabilities = st.number_input('**Total Fund Liabilities ($)**',
                                  value= 50000,
                                  help='Money owes by the fund at the moment including daily management fees, administrative costs or borrowed money')
    



shares = container.number_input('**Total Shares Outstanding**',
                             value= 10000,
                             help='The exact number or individual ETF shares that have ben created and are currently held by investors')

    


is_stale = container.checkbox('**Check for Stale Pricing?**',
                              help='Warns users that the NAV might be lagging behind real-time market conditions')

st.write('---')

nav = get_nav(assets, liabilities, shares)

container2 = st.container(border=True)

container2.metric('**NET ASSET VALUE (NAV)**',
                  value= f'${nav:.2f} per share',help= 'The true book value of a single ETF share. ' \
                  'If the fund sold all its assets and paid off all liabilites, this is exactly how much cash one share would be worth')


if is_stale:
    container3 = st.container(border=True)
    container3.warning("**Stale Price Alert** \n\n "
    "if underlying asset prices are stale, the calculated NAV is a 'lagging' indicator. Traders may exploit this difference through arbitrage ")





st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")