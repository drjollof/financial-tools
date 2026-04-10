import streamlit as st

def get_metrics(a, d):
    eq = a - d
    lev = (a / eq) if eq > 0 else float('inf')
    good = eq > 0

    return eq, lev, good

def price_floor(L,S,F, margin):
    total = L + S + F

    target = total * (1 + margin /100)
    profit = target - total
        
    return total,target, profit


st.header('Leverage and Development Lab')
st.divider()
 
col1, col2 = st.columns(2,  border=True)

with col1:
    st.subheader('Homeowner Equity')
    asset = st.number_input('**Total Asset Value ($)**',
                            value= 500000,
                            format='%d',
                            help='current house price')
    
    debt = st.number_input('**Total Liabilities ($)**',
                            value= 350000,
                            format = '%d',
                            help='remaining mortgage')
    st.divider()

    equity , leverage , status = get_metrics(asset, debt)
    container1 = st.container(border=True)
    container2 = st.container(border=True)

    container1.metric('**Net Equity**', f"{'-' if equity < 0 else ''}${abs(equity):,.0f}",
              delta='Healthy Buffer' if status else 'Negative Equity',
              delta_color='normal' if status else 'inverse',
              help='true ownership value of asset')
    
    

    if status:
        container2.metric('Equity Multiplier', f'{leverage:.1f}x',
                  help=f'This means for every 1 of your own money, you control ${leverage:.2f} of assets.')
        
    else:
        st.error('Net equity is zero or negaitve. Thus equity multiplier is undefined')


with col2:
    st.subheader('Developer Price Floor')
    land = st.number_input('Land Costs ($)',
                    value=40000,
                    format='%d',
                    help='Land Acquisition')
    
    hard = st.number_input('Hard Cost ($)', 
                    value=50000,
                    format='%d',
                    help='construction materials, labor')
    
    soft = st.number_input('Soft Cost ($)', 
                    value=70000,
                    format='%d',
                    help='permits,fees')
    
    margin_pct = st.slider('**Profit Margin (%)**', 0, 100, 15, step=1)

    st.divider()

    break_even, target, profit = price_floor(land, hard, soft, margin_pct)
    container3 = st.container(border=True)
    container4 = st.container(border=True)

    container3.metric('**Break-even Price**', 
              f'${break_even:,.0f}',
              help='This is the absolute minimum sale price to avoid a loss')
    
    

    container4.metric(f'**Target Sale Price**',
              f'${target:,.0f}',
              delta=f"${profit:,.0f}",
              delta_color='normal',
              help=f'with {margin_pct}% margin')
    



    
    
st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")