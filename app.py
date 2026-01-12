import streamlit as st


bond_page = st.Page(
    page='pages/bond.py',
    title='Bond Price Calculator',
    default=True
)

inflation_page = st.Page(
    page='pages/inflation_return.py',
    title='Inflation'
)

short_page = st.Page(
    page= 'pages/short_selling.py',
    title='Short Selling')

cb_page = st.Page(
    page= 'pages/central_bank.py',
    title='CBR'
)

nav = st.navigation(
    {
      'Module 1' : [bond_page, inflation_page, short_page, cb_page]
    }
)
st.sidebar.text('Made by drjollof')

nav.run()





