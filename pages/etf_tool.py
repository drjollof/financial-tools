import streamlit as st


def get_nav(assets, liabilities, shares):

    return (assets - liabilities) / shares



st.header('ETF Net Asset Value (NAV) Calculator')
container = st.container(border=True)
col1, col2, col3 = container.columns(3, border=True)

with col1:
    assets = st.number_input('**Total Assets**',
                             value= 5000)

with col2:
    liabilities = st.number_input('**Total Liabilities**',
                                  value= 2000)

with col3:
    shares = st.number_input('**Shares Outstanding**',
                             value= 40)



nav = get_nav(assets, liabilities, shares)

container2 = st.container(border=True)
col4, col5, col6 = container2.columns(3)

with col5:
    st.metric('**NAV per Share ($)**', 
              value = f'{nav:.0f}')