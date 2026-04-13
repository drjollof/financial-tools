import streamlit as st

st.header('Technical Analysis')

st.markdown("""
*Track simple price momentum to spot trends, and test how the RSI indicator flags 'overbought' or 'oversold' conditions.*
""")

st.divider()

col1, col2 = st.columns(2, border=True)

with col1:
    today_price = st.number_input("**Price_today ($)**",
                                   value =100,
                                     help='The current trading price of the asset in the open market today')
    
    price_30 = st.number_input('**Price_30d ($)**',
                                value = 90,
                                help='The price exactly one month ago. We use this to measure how fast the price is moving in the short term')
    

with col2:
    price_60 = st.number_input('**Price_60d ($)**',
                                value= 75,
                                help='The price two months ago. Comparing this to the 30-day price helps us see if a trend is speeding up or running out of steam')
    
    rsi = st.slider('**Current RSI Level**',
                     value=75,
                       help='The Relative Strength Index (RSI) is a momentum score from 0 to 100. It measures the speed and change of recent price movements to see if investors are overreacting')



st.divider()

mom_30d = today_price - price_30
mom_60d = today_price - price_60

mcol1, mcol2 = st.columns(2, border=True)

with mcol1:
    st.metric('30-Day Momentum', f'{mom_30d:+.0f}',
              delta= 'Accelerating' if mom_30d > mom_60d and mom_30d > 0 else 'Slowing' if mom_30d < mom_60d > 0 else None,
              delta_color='normal' if mom_30d >= 0 else 'inverse',
              help='The raw dollar difference over the last month')
    
with mcol2:
    st.metric('**60-Day Momentum**', f'{mom_60d:+.0f}', help= 'The raw dollar difference over the last two months')


if rsi > 70:
    st.error("**OVERBOUGHT**\n\n"
             "***RSI above 70 indicates the asset may be overvalued by recent buyers "
             "and could be due for a pullback or correction***")
elif rsi < 30:
    st.success('**OVERSOLD**\n\n'
               '***RSI below 30 indicated the asset has been heavily sold '
               'and might be ready for a rebound or reversal upward***')
    
else:
    st.info('**NEUTRAL**\n\n'
            '***RSI between 30-70 suggests the asset is trading in a normal range.***\n\n'
            '***No strong momentum extreme at the moment***')





st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")