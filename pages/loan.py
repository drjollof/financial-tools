import streamlit as st

st.title('Loan Underwriting Simulator')

st.markdown("""
*Evaluate individual borrower creditworthiness for mortgage. 
            Use Loan-to-Value (LTV) and Debt-to-Income (DTI) ratios to assess financial capacity, collateral strength, and baseline default risk before funding*
""")

st.divider()

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
    st.subheader('**Capacity (DTI Ratio)**')
    st.divider()
    income = st.number_input('**Monthly Gross Income ($)**', 
                             value= 6000,
                               help="The borrower's total income before taxes and any other deductions are taken out.")
    
    debt = st.number_input('**Total Monthly Debt Payments ($)**',
                           value=2400,
                             help="All of the borrower's existing monthly debt (car loans, credit cards) plus the proposed new mortgage payment.")

    dti = calc_dti(debt, income)
    st.divider()
    if dti >= 50:
        st.error(f'**DTI Ratio: {dti}%**')

    elif dti > 43:
       st.warning(f'**DTI Ratio: {dti}%**')
    
    else:
       st.success(f'**DTI Ratio: {dti}%**') 

with col2:
    st.subheader('**Collateral (LTV Ratio)**')
    st.divider()
    house_val = st.number_input('**House Price ($)**',
                                 value=500000,
                                   help='The current market value of the property')
    
    loan_amt = st.number_input('**Loan Amount ($)**',
                                value=400000,
                                  help='The total amount of money the borrower is asking the bank to lend them')
    
    ltv = calc_ltv(loan_amt, house_val)

    st.divider()

    if ltv >= 100:
       st.error(f'**LTV Ratio: {ltv:.1f}%**')

    elif ltv > 80:
       st.warning(f'**LTV Ratio: {ltv:.1f}%**')

    else:
       st.success(f'**LTV Ratio: {ltv:.1f}%**')
      


st.subheader("Final Underwriting Decision")


if dti < 43 and ltv <= 80:
    st.info("**Decision: Approved**")

elif dti >= 50 or ltv >= 100:
    st.error("**Decision: Declined**")
else:
    st.warning("**Decision: Flagged for Manual Review**")






st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")