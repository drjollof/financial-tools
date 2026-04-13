import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def plot_payoff(s_current, strike, premium, option_type, position):
    
    lower_bound = min(strike, s_current) * 0.5
    upper_bound = max(strike, s_current) * 1.2
    s_t = np.linspace(lower_bound, upper_bound, 100)
    
    
    if option_type == "Call":
        payoff = np.maximum(s_t - strike, 0)
    else: 
        payoff = np.maximum(strike - s_t, 0)
    
    if position == "Long":
        profit = payoff - premium
    else: 
        profit = premium - payoff

    fig, ax = plt.subplots(figsize=(10, 6), dpi = 100)
    ax.plot(s_t, profit, color='#00d4ff', linewidth=2)
    ax.axhline(0, color='white', lw=1, ls='--') 

    ax.axvline(strike, color='grey', lw=1, ls='--', ) 

    ax.text(strike, ax.get_ylim()[1]*0.4, 'Strike price' , color = 'grey', 
            fontweight = 'normal',
            ha = 'right', va = 'center',
            rotation = 90)
    
    ax.axvline(s_current, color='#ffcc00', lw=1, ls='--')
    ax.text(s_current, ax.get_ylim()[1]*0.4, 'Stock price', 
            color='#ffcc00', fontweight='normal',
            rotation = 90, va = 'center', ha = 'right')

    
    ax.fill_between(s_t, profit, 0, where=(profit > 0),
                     color='green', alpha=0.3)
    ax.fill_between(s_t, profit, 0, where=(profit < 0), 
                    color='red', alpha=0.3)

    
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    ax.set_xlabel("Stock Price at Expiration ($S_T$)", color='white')
    ax.set_ylabel("Profit / Loss ($)", color='white')
    ax.tick_params(colors='white')
    
    return fig

def get_metrics(s_current, strike, premium, option_type, position):
    intrinsic = np.maximum(0, s_current - strike) if option_type == 'Call' else np.maximum(0, strike - s_current)
    breakeven = (strike + premium) if option_type == 'Call' else (strike - premium)
    net_pl = (intrinsic - premium) if position == 'Long' else (premium - intrinsic)

    if position == 'Long':
        max_risk_val = -premium * 100
        risk_label = 'Premium Paid'
    elif position == 'Short' and option_type == 'Call':
        max_risk_val = 'UNLIMITED'
        risk_label = 'Potential for Catastrophic Loss'
    else:
        max_risk_val = -(strike - premium) * 100
        risk_label =  'Strike - Premium'

    return intrinsic, breakeven, net_pl, max_risk_val, risk_label

# 
st.title('Option Payoff Visualizer')

st.markdown(""" 
*Visualize the profit and loss profiles of call and put options using "Hockey Stick" payoff. Evaluate risk-reward scenarios where buyer losses are capped at the premium, a key concept for managing trade volatility* """
)
st.divider()

col1, col2, col3 = st.columns(3, border=True)

with col1:
    st.subheader('Assets')
    asset_price = st.number_input('**Stock Price ($)**',
                                  help='The current market price of the asset')
    s_p = st.number_input('**Strike Price ($)**',
                          help='The pre-agreed price at which you can exercise your right to buy or sell regardless of market fluctuations')


with col2:
    st.subheader('Contract Type')
    op_type = st.selectbox('**Option Type**', options=['Call', 'Put'], help='Select Call if you want the right to buy the asset, or Put if you want the right to sell it.')
    pos = st.selectbox('**Position**', ['Long', 'Short'], help='Choose Long if you are the buyer (limited risk) or Short if you are the seller/writer (potentially high risk).')

with col3:
    st.subheader('Premium Paid')
    premium = st.number_input('**Premium ($)**', help='The "entry fee" or market price you pay per share to own this contract.')

container = st.container(border=True)

container.subheader("Hockey Stick Payoff Chart")
container.pyplot(plot_payoff(asset_price, s_p, premium, op_type, pos))
iv, bp, net, mrv, rl= get_metrics(asset_price, s_p, premium, op_type, pos)
    
if asset_price > s_p:
    container.success('**Option is in the money**')
elif asset_price == s_p:
    container.info('**Option is at the money**')
else: 
    container.error('**Option is out of the Money**')

st.divider()
col5,col6,col7,col8 = st.columns(4, border=True)



with col5:
    st.metric('**Intrinsic Value**', f'${iv:.2f}', help='The immediate "cash value" of the option if you used it right now')

with col6:
    st.metric('**Breakeven Point**', f'${bp:.2f}', help='The stock price at which your profit exactly covers the cost of the premium.')

with col7:
    st.metric('**Net P/L**', f'${net:.2f}', help='Total profit or loss after subtracting the premium paid from the payoff')

with col8:
    if isinstance(mrv, str):
        st.metric('**Max Risk**', f'{mrv}', help='The absolute most you can lose on this trade (for buyers, this is just the premium)')
        st.text(rl)
    else:
        st.metric('**Max Risk**', f'${mrv:.1f}' , help='The absolute most you can lose on this trade (for buyers, this is just the premium)')
        st.text(rl)




st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")