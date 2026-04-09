import streamlit as st


st.title("Fractional Reserve Banking Simulator")
st.caption(f"*Calculations assume a closed banking system where all lent money is re-deposited.*")



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
    

st.subheader("Bank Parameters")
col1, col2, col3 = st.columns(3 , border=True)

with col1:
    initial_deposit = st.number_input("Initial Deposit ($)", 
                                      value=10000, 
                                      )
with col2:
    reserve_ratio = st.slider("Reserve Ratio (%)",
                               1, 50, 10,
                                 help="The % of deposits the bank must keep in the vault.")
with col3:
    interest_margin = st.slider("Interest Margin (%)", 
                                0.5, 10.0, 4.0, 
                                help="The profit gap between loan rates and deposit rates.")


total_system_deposits , annual_profit , multiplier, liquidity_buffer = get_metrics(reserve_ratio, initial_deposit, interest_margin)

st.write("---")
m1, m2, m3 = st.columns(3, border=True)


m1.metric("Total System Deposits",
           value= f"${total_system_deposits:,.0f}",
           help=f"Money Multiplier: {multiplier:.0f}x")

m2.metric("Bank Annual Profit",
          value=  f"${annual_profit:,.0f}",
            help="Estimated income from re-lending deposits.")

m3.metric("Liquidity Buffer", 
          value= f"${initial_deposit:,.0f}",
           
            help="The actual cash available for withdrawals.")



st.write("---")
st.subheader("Withdrawal Stress Test")

container1 = st.container(border=True)

container2 = st.container(border=True)
col4 = st.columns(1, border=True)

withdrawal_percent = container1.slider(" **Percentage Withdrawal (%)** ",
                                    help="What % of customers want their cash back at the same time?")


withdrawal_amount = get_stress_test(withdrawal_percent, total_system_deposits)



if withdrawal_amount <= initial_deposit:
    container2.success(f"**STABLE** \n\n **The bank has enough liquidity to cover ${withdrawal_amount:,.0f} in withdrawals** ")

else:
    container2.error("**INSOLVENT** \n\n  **Withdrawals exceed available cash** ")
    st.divider()
    container2.warning("**LIQUIDITY CRISIS** \n\n **You would need an emergency loan from the Central Bank** ")





