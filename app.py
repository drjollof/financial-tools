import streamlit as st
defaults  = {'w_a' : 50,
             'w_b' : 50,
             'r_a' : 10,
             'r_b': 12, 
             'vol_a' : 20,
             'vol_b' : 30,
             'corr' : 0.2,
             'port_vol' : 0,
             'port_return': 0,
             'port_var' : 0
             }

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

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

returns_page = st.Page(
    page= 'pages/returns_lab.py',
    title='Returns'
)

sharpe_page = st.Page(
    page= 'pages/sharpe_analyzer.py',
    title= 'Sharpe-Ratio'
)

valuation_page = st.Page(
    page= 'pages/valuation_models.py',
    title= 'Valuation'
)

portfolio_page = st.Page(
    page='pages/portfolio.py',
    title='Porfolio Simulator'
)

etf_page = st.Page(
    page= 'pages/etf_tool.py',
    title='ETF Evaluation Tool'
)

beta_page = st.Page(
    page='pages/beta_analysis.py',
    title='Portfolio Performane Metrics'
)

nav = st.navigation(
    {
      'Module 1' : [bond_page, inflation_page, short_page, cb_page],
      'Module 2' : [returns_page, valuation_page , sharpe_page],
      'Module 3' : [portfolio_page, beta_page, etf_page]
    }
)
st.sidebar.text('Made by drjollof')

nav.run()





