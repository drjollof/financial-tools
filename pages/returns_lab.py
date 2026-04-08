import streamlit as st
import math

def get_metrics(initial_price,final_price, dividend , is_dividend = False):
  if is_dividend:
    ar_return = (final_price + dividend - initial_price) /initial_price
    log_return = math.log((final_price + dividend) / initial_price)
    div_yield = dividend/final_price
  else:
    ar_return = (final_price - initial_price)/initial_price
    log_return = math.log((final_price)/initial_price)
    div_yield = 0

  return ar_return * 100 , log_return * 100 , div_yield * 100





st.header('Returns and Performance')
st.divider()

col1, col2 = st.columns(2, border=True)
with col1:
  i_p = st.number_input('**Initial Price($)**',
                        value= 60,
                        help = 'The purchase price per share at the beginning of the period.')

with col2:
  f_p = st.number_input('**Final Price ($)**', value= 70,
                        help='The market price per share at the end of the period (the price at which you sold the asset)')
    
is_dividend = st.toggle('**Include Dividends**', 
                          help='Toggle this to include dividend received while holding the asset')

if is_dividend:
 div = st.number_input('**Dividend Amount ($)**', 
                       value= 4,
                       help='Total cash value of dividend received per share')
 arithmetic_return , logarithmic_return, dividend_yield = get_metrics(i_p, f_p, div, True)
 

else: 
  arithmetic_return , logarithmic_return , dividend_yield = get_metrics(i_p, f_p, 0,  False)
 
st.divider()

col3, col4, col5 = st.columns(3, border= True, width='stretch')
with col3:
  st.metric('**Arithmetic Return**',
             f'{arithmetic_return:.2f}%',
             delta= f'{arithmetic_return:.2f}%',
             delta_color= 'normal' ,
             help='The standard percentage gain or loss'
            )

with col4:
  st.metric('**Logarithmic Return**',
             f'{logarithmic_return:.2f}%',
             delta= f'{logarithmic_return:.2f}%',
             delta_color= 'normal',
             help='The continously compounded return..mathematically additive and symmetric over time.')
with col5:
  st.metric('**Dividend Yield**',
             f'{dividend_yield:.2f}%',
             help='The income-generating efficiency of the asset. Shows how much cash received relative to the price paid.')