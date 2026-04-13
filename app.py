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
    title='Bond Pricing',
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
    title='Central Bank Reserve'
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
    title= 'Valuation models'
)

portfolio_page = st.Page(
    page='pages/portfolio.py',
    title='Porfolio Simulator'
)

etf_page = st.Page(
    page= 'pages/etf_tool.py',
    title='ETF Evaluation'
)

beta_page = st.Page(
    page='pages/beta_analysis.py',
    title='Portfolio Performance'
)

payoff_page = st.Page(
    page='pages/option_payoff.py',
    title='Payoff Visualizer'
)

parity_page = st.Page(
    page='pages/put_parity.py',
    title='Put Call Parity'
)

merton_page = st.Page(
    page='pages/merton_model.py',
    title='Merton Model Simulator'
)

loan_page = st.Page(
    page='pages/loan.py',
    title='Loan Evaluator'
)

mbs_page = st.Page(
    page='pages/mbs_sim.py',
    title='MBS Simulator'
)

credit_page = st.Page(
    page= 'pages/credit_risk.py',
    title= 'Credit Risk'
)

leverage_page = st.Page(
    page= 'pages/leverage.py',
    title='Leverage and Development'
)

equity_page = st.Page(
    page='pages/equity.py',
    title= 'Equity Research'
)

ta_page = st.Page(
    page= 'pages/ta.py',
    title='Technical Analysis'
)

nav = st.navigation(
    {
      'Module 1' : [bond_page, inflation_page, short_page, cb_page],
      'Module 2' : [returns_page, valuation_page , sharpe_page],
      'Module 3' : [portfolio_page, beta_page, etf_page],
      'Module 4' : [payoff_page, parity_page, merton_page],
      'Module 5' : [loan_page, mbs_page, credit_page ],
      'Module 6' : [leverage_page, equity_page, ta_page]
    }
)
st.sidebar.text('Made by drjollof')

nav.run()





