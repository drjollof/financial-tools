import streamlit as st


st.title("Fractional Reserve Banking Simulator")

st.markdown("""
*Simulate deposits multiplier effect and how credit is created through systemic lending. 
            Use the Stress Test to determine if the bank’s physical liquidity can survive a sudden digital bank run.*
""")


st.caption(f"*Calculations assume a closed banking system where all lent money is re-deposited.*")

st.divider()


def get_metrics(reserve_ratio, initial_deposit, interest_margin):

    multiplier = 1 / (reserve_ratio / 100)
    total_system_deposits = initial_deposit * multiplier

    total_loans = total_system_deposits * (1 - (reserve_ratio / 100))
    annual_profit = total_loans * (interest_margin / 100)

    liquidity_buffer = initial_deposit * (reserve_ratio / 100)


    return total_system_deposits , annual_profit , multiplier , liquidity_buffer


def get_stress_test(withdrawal_percent, total_system_deposits):
    withdrawal_amount = total_system_deposits * (withdrawal_percent / 100)

    return withdrawal_amount
    


container0 = st.container(border=True)

container0.subheader("Bank Parameters")

col1, col2, col3 = container0.columns(3 , border=True)

with col1:
    initial_deposit = st.number_input("**Initial Deposit ($)**", 
                                      value=10000, 
                                      )
with col2:
    reserve_ratio = st.slider("**Reserve Ratio (%)**",
                               1, 50, 10,
                                 help="The % of deposits the bank must keep in the vault.")
with col3:
    interest_margin = st.slider("**Interest Margin (%)**", 
                                0.5, 10.0, 4.0, 
                                help="The profit gap between loan rates and deposit rates.")


total_system_deposits , annual_profit , multiplier, liquidity_buffer = get_metrics(reserve_ratio, initial_deposit, interest_margin)

st.write("---")
m1, m2, m3 = st.columns(3, border=True)


m1.metric("**Total System Deposits**",
           value= f"${total_system_deposits:,.0f}",
           help=f"""The aggregate value of all digital account balances generated through the lending cycle. 
           This value represents the total credit supply in the system.     

             Money Multiplier: {multiplier:.0f}x""")

m2.metric("**Bank Annual Profit**",
          value=  f"${annual_profit:,.0f}",
            help="Estimated income from re-lending deposits.")

m3.metric("**Liquidity Buffer**", 
          value= f"${initial_deposit:,.0f}",
           
            help="The actual cash available for withdrawals.")



st.write("---")
st.subheader("Withdrawal Stress Test")

container1 = st.container(border=True)

container2 = st.container(border=True)
col4 = st.columns(1, border=True)

withdrawal_percent = container1.slider(" **Percentage Withdrawal (%)** ",
                                    help=f"""
    The proportion of total account balances customers attempt to withdraw at once. 
    
    In a fractional reserve system, the bank is insolvent if the withdrawal amount 
    exceeds the physical cash in the vault. 
    
    Current Failure Point: > {reserve_ratio}% withdrawal demand.
    """)


withdrawal_amount = get_stress_test(withdrawal_percent, total_system_deposits)



if withdrawal_amount <= initial_deposit:
    container2.success(f"**STABLE** \n\n **The bank has enough liquidity to cover ${withdrawal_amount:,.0f} in withdrawals** ")

else:
    container2.error("**INSOLVENT** \n\n  **Withdrawals exceed available cash** ")
    container2.warning("**LIQUIDITY CRISIS** \n\n **You would need an emergency loan from the Central Bank** ")





st.markdown("---")
st.caption("""
**Disclaimer:** This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")