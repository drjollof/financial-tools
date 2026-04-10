import streamlit as st
import pandas as pd

st.title('Short Selling Analysis')

st.markdown("""
*Simulate profits from falling market prices by tracking the short selling cycle.
             Monitor financing fees and dividend obligations while watching the Margin Call price to manage unlimited risk*
""")

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


def margin_call(initial_price, initial_margin_pct,maint_margin_pct):

    if initial_margin_pct > 0:



        margin_call_price = initial_price * ((1 + initial_margin_pct/100) / (1 + maint_margin_pct/100))
        
        
        gross_pl = (initial_price - current_price) * shares
        percent_pl = (gross_pl / (initial_price * shares * (initial_margin_pct/100))) * 100

    else:
        margin_call_price = 0
        gross_pl = 0
        percent_pl = 0

    return margin_call_price, gross_pl, percent_pl


col1 , col2 = st.columns(2, border=True)


with col1:
    st.subheader("Position Details")
    st.write('---')
    initial_short_price  = st.number_input('**Initial Short Price ($)**',
                          value=200,
                           help='The price at which you borrowed and sold the shares' )
    
    shares = st.number_input('**Number of Shares**',
                             value=100,
                             help='Total number of shares')
    
    current_price = st.number_input('**Cover Price ($)**',
                          value=180,
                          help='The price you pay to buy the shares back and return them to the lender')
    
    
    D_p = st.number_input('**Dividend Per Share ($)**',
                          value=2,
                          help='Dividends paid by the company while you are short the stock')
    
    H_p = st.number_input('**Holding Period (days)**',
                          value= 30,
                          help='The number of days you plan to keep the short position open')
    
    F_r = st.slider('**Financing Rate (%)**',
                    value=3,
                    help='The rental fee paid to your broker for borrowing the shares')
    


    g_profit = gross_profit_fn(initial_short_price, current_price, shares)
    income_cost , financing_cost, market_value = short_cost_fn(D_p, shares, H_p, initial_short_price, F_r )
    net_profit = net_profit_fn(g_profit, income_cost, financing_cost)

    if market_value >0 :
        roi = (net_profit/market_value) * 100
    else:
        roi = 0

    data = {'**Gross Profit/Loss**' : f'${g_profit:.2f}',
             '**Financing Cost**': f'${financing_cost:.2f}',
             '**Income Cost**' : f'${income_cost:.2f}'
             }

with col2:
    
    st.metric('**Net Profit/Loss:**', value= f'${net_profit:.2f}', delta=f'{roi:.2f}%', border=True )
    st.write('---')
    st.subheader('**P/L Breakdown**')
    st.table(data,)
    st.write('---')

    st.warning('Warning: Short selling involves unlimited risk. Ensure sufficient margin to avoid liquidation')


st.divider()

col_left, col_right = st.columns(2, border=True)


with col_left:
    
    st.subheader("Margin Settings")
    st.write('---')

    
    initial_margin_pct = st.slider("**Initial Margin (%)**", 
                                   value= 50, 
                                   help="Cash you put up upfront.")
    
    maint_margin_pct = st.slider("**Maintenance Margin (%)**",
                                  value= 30,
                                  help="Minimum safety level before a Margin Call.")



with col_right:

    gross_pl , percent_pl, margin_price = margin_call(initial_short_price, initial_margin_pct, maint_margin_pct)

    st.subheader("Liquidation Risk")
    
    st.write('---')
    st.metric('**Margin Call Price:**' , f'${margin_price:,.2f}',
               border=True,
               help='If the stock hits this price, the broker will force-close your position.')



    price_gap = margin_price - current_price
    st.write('---')
    
    if current_price >= margin_price:
        st.error(" **MARGIN CALL TRIGGERED: Your position is being liquidated** ")

    elif price_gap < (initial_short_price * 0.05):

        st.warning(f" **CRITICAL: You are only ${price_gap:,.2f} away from a Margin Call!** ")

    else:
        st.success(f" **Position is currently stable. You have a ${price_gap:,.2f} safety buffer** ")




st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")

