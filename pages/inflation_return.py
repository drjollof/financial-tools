import streamlit as st

st.title('Inflation & Real Returns')

st.markdown("""
*Calculate the true growth of your wealth by adjusting nominal gains for inflation. 
            Use this to see the actual purchasing power of deposits after accounting for inflation.*
""")



def calc_metrics(initial_deposit, nominal_rate, inflation_rate, time):
    p_inf = inflation_rate/100
    p_nom = nominal_rate/100
    nominal_bal = (initial_deposit) * (1+ p_nom) ** time
    nominal_profit = nominal_bal - initial_deposit

    inflation_bal = (nominal_bal)/ (1+ p_inf) ** time
    inflation_loss = nominal_bal - inflation_bal

    net_real_gain = nominal_profit - inflation_loss

    real_rate_of_return = ((1 + p_nom)/ (1 + p_inf)) - 1

    purchasing_power = (1 + real_rate_of_return) ** time

    v_0 = (initial_deposit)/ (1+ p_inf) ** time
    v_1 = (initial_deposit)/ (1+ (real_rate_of_return/100))**time

    p0_loss = ((initial_deposit - v_0)/initial_deposit ) * 100
    p1_loss = ((inflation_bal - initial_deposit) / initial_deposit) * 100



    
    return nominal_profit, inflation_loss, net_real_gain, real_rate_of_return * 100, p0_loss, p1_loss, purchasing_power


st.divider()

col1 , col2 = st.columns(2, border= True)

with col1:
    id = st.number_input('**Initial Deposit ($)**', value= 10000,
                         help='')
    
    ir = st.slider('**Inflation Rate(%)**', min_value= 0.0, 
                   max_value=20.0, 
                   value= 1.0,
                   step=0.10,
                   help='how much price are rising each year' )
    

    nir = st.slider('**Nominal Rate(%)**', min_value= 0.0, max_value=20.0,
                    step=0.10,  
                    value= 6.0,
                    help='the profit rate your bank or bond offers')
    
    t = st.slider('Time Horizon (years)', value=3,
                  help='Total duration your money remains deposited')
    
   

with col2:
    n_p, i_l, n_g , r_r, p_0, p_1, p_p = calc_metrics(id, nir, ir, t)

    st.metric(label='**REAL RETURN**', value = f'{r_r:.2f}%',
              help='The actual growth of the deposit after removing the impact of inflation')
    st.write("---")


    if n_g > 0:
        st.success(f"**You are outrunning inflation!** \n\n **Your wealth is growing by {r_r:.2f}% annually.**")
    elif n_g == 0:
            st.warning("**You are exactly breaking even!** \n\n" \
            " **You aren't getting richer, you're just keeping pace.**")

    else:
            st.error(f"**Inflation is winning!** \n\n **You are losing {abs(r_r):.2f}% of your wealth annually**")




  
st.divider()
m1, m2, m3 = st.columns(3, border=True)
m1.metric("**Nominal Gain**", f"+${n_p:,.0f}", 
          help="Total gain before inflation. Tax excluded")

m2.metric("**Inflation Impact**", f"-${i_l:,.0f}", 
          delta_color="inverse", 
          help="Value eroded by rising prices.")

m3.metric("**Real Gain/Loss**", f"{'-' if n_g < 0 else ''}${abs(n_g):,.0f}", 
          help="Actual increase in purchasing power.")


container = st.container(border=True)

if p_1 < 0:
    container.info(f'At a moderate {ir}% inflation rate, a ${id:,.0f} deposit left idle for {t} years without {nir}% interest rate would lose about {p_0:.2f}% of its value. \n\n While  the same deposit with {nir}% interest rate would lose about {abs(p_1):.2f}% of its value. ')

else:
  container.info(f'At a moderate {ir}% inflation rate, a ${id:,.0f} deposit left idle for {t} years without {nir}% interest rate would lose about {p_0:.2f}% of its value. \n\n While  the same deposit with {nir}% interest rate would gain about {abs(p_1):.2f}% of its value. ')









st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")