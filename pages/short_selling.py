import streamlit as st

st.header('Short Position P/L Analysis')
st.divider()

def gross_profit_fn(initial_price, cover_price, n_shares):
    return (initial_price - cover_price)*n_shares


def short_cost_fn(coupon_paid, shares, holding_days,
                initial_price, finacing_rate):
    income_cost = (coupon_paid * shares * holding_days)/365
    market_value = initial_price * shares
    financing_cost = (market_value * finacing_rate/100 * holding_days)/365
    return income_cost, financing_cost, market_value


def net_profit_fn(gross_profit, finacing_cost, income_cost):
    return gross_profit - (finacing_cost + income_cost)



col1 , col2 = st.columns(2, border=True)

with col1:
    st.subheader('Trade Parameters')
    st.divider()
    isp = st.number_input('Initial Short Price ($)')
    shares = st.number_input('Number of shares')
    cp = st.number_input('Cover Price ($)')
    F_r = st.slider('Financing Rate (%)')
    D_p = st.number_input('Dividend per share ($)')
    H_p = st.number_input('Holding Period (days)')


    g_profit = gross_profit_fn(isp, cp, shares)
    income_cost , financing_cost, market_value = short_cost_fn(D_p, shares, H_p, isp, F_r )
    net_profit = net_profit_fn(g_profit, income_cost, financing_cost)

    if market_value >0 :
        roi = (net_profit/market_value) * 100
    else:
        roi = 0

    data = {'Gross Profit' : f'${g_profit:.2f}',
             'Financing Cost': f'${financing_cost:.2f}',
             'Income Cost' : f'${income_cost:.2f}'
             }

with col2:
    st.subheader('Profit/Loss Summary')
    st.divider()
    st.metric('Net Profit', value= f'${net_profit:.2f}', delta=f'{roi:.2f}%', border=True )
    st.divider()
    st.subheader('P/L Breakdown')
    st.table(data,)

    st.warning('Warning: Short selling involves unlimited risk. Ensure sufficient margin to avoid liquidation')


st.divider()


