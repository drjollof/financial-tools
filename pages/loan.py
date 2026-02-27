import streamlit as st

st.title('Loan Underwriting Analysis')

def calc_ltv(loan_amount, house_value):
    if house_value <= 0:
     return 0
    
    else:
        return (loan_amount/house_value) * 100
    

def calc_dti(monthly_debt, monthly_income):
   if monthly_income <= 0:
      return 0
   else:
      return (monthly_debt / monthly_income) * 100

col1 , col2 = st.columns(2, border=True)

with col1:
    st.write('**Capacity (DTI Ratio)**')
    income = st.number_input('Monthly Gross Income ($)', value= 6000)
    debt = st.number_input('Total Monthly Debt Payments ($)',value=2400)

    dti = calc_dti(debt, income)
    st.divider()
    if dti >= 50:
        st.error(f'DTI Ratio: {dti}%')

    elif dti > 43:
       st.warning(f'DTI Ratio: {dti}%')
    
    else:
       st.success(f'**DTI Ratio: {dti}%**') 

with col2:
    st.write('Collateral (LTV Ratio)')
    house_val = st.number_input('House Price ($)', value=500000)
    loan_amt = st.number_input('Loan Amount ($)', value=400000)
    ltv = calc_ltv(loan_amt, house_val)

    st.divider()

    if ltv >= 100:
       st.error(f'LTV Ratio: {ltv:.1f}%')

    elif ltv > 80:
       st.warning(f'LTV Ratio: {ltv:.1f}%')

    else:
       st.success(f'LTV Ratio: {ltv:.1f}%')
      


st.header("Final Underwriting Decision")


if dti < 43 and ltv <= 80:
    st.info("**Decision: Approved**")

elif dti >= 50 or ltv >= 100:
    st.error("**Decision: Declined**")
else:
    st.warning("**Decision: Flagged for Manual Review**")