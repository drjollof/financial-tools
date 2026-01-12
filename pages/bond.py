import streamlit as st

st.header('Bond Pricing & Interest Rate Sensitivity')
st.write('This app calculates the price of a bond based on its parameters.')


def calculate_bond_price(face_value, coupon_rate, years_to_maturity, market_rate):
    coupon_payment = face_value * coupon_rate/100

    price = 0
    for t in range(1, years_to_maturity + 1):
        price += coupon_payment / (1 + market_rate/100) ** t
    price += face_value / (1 + market_rate/100) ** years_to_maturity
    return round(price, 2) 
st.divider()

col1,col2 = st.columns(2, border=True)


with col1:
    
        fv = st.number_input('Par value ($)',
                             placeholder='Enter bond face value...')
        c_rate = st.slider('Coupon Rate (%)')
        maturity = st.slider('YTM (years)')
        mr = st.slider('Market Interest Rate (%)')
        
    
with col2:
     with st.container():
        bp = calculate_bond_price(fv, c_rate, maturity, mr)
        st.metric(label='Bond Price:', value=f'${bp}',width= 'content' )
        if bp < fv:
            st.success('Discount')
           
        else:
            st.warning('Premium')

     st.info('As interest rates rise, bond prices fall', icon="ℹ️")
     

