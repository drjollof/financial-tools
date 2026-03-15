import streamlit as st

st.header('Bond Pricing')

def get_bond_price(face_value, coupon_rate, years_to_maturity, market_rate):
    coupon_payment = face_value * coupon_rate/100

    price = 0
    for t in range(1, years_to_maturity + 1):
        price += coupon_payment / (1 + market_rate/100) ** t
    price += face_value / (1 + market_rate/100) ** years_to_maturity
    return round(price, 2) 


def get_bond_sensitivity(mod_duration, dr, dollar_duration, convexity):
    relative_change = -mod_duration * dr
    

    first_order_abs = -dollar_duration * dr
    

    second_order_abs = first_order_abs + (0.5 * convexity * (dr ** 2))

    return relative_change, first_order_abs, second_order_abs



st.divider()

col1,col2 = st.columns(2, border=True)


with col1:
    
        fv = st.number_input('**Par value ($)**',
                             value= 800,
                             help='The total amount the bond will be worth when it expires'
                             )
        
        c_rate = st.slider('**Coupon Rate (%)**',
                           value=6,
                           help='The fixed annual payment the bond pays'
                           )

        maturity = st.slider('**Years to Maturity (years)**',
                             value=2,
                             help='the number of years left until bond issuer pays back the full par value'
                             )
        
        mr = st.slider('**Interest Rate (%)**',
                       value=4,
                       help='The current rate for new bonds issued in the market')
        
    
with col2:
     with st.container():
        bp = get_bond_price(fv, c_rate, maturity, mr)

        container1 = st.container(border=True)
        container2 = st.container(border=True)
    

        container1.metric('**Bond Price**', value=f'${bp}', 
                          width= 'content',
                          help='Current worth of the bond ')

        if bp < fv:
            container2.success('** Trading at Discount**')
           
        else:
            container2.warning('**Trading at a Premium**')


        container2.info('**As interest rates rises, bond prices falls**')
     


st.divider()


st.header('Interest Rate Sensitivity')
st.divider()

col3, col4, col5 = st.columns(3, border=True)

with col3:
    m_d = st.number_input(
        "**Modified Duration (MD)**", 
        value=7.55, 
        help="Measures percentage price sensitivity. \n\n " \
        "E.g., 7.55 means a 1% rate hike causes roughly a 7.55% price drop."
    )
with col4:
    d_d = st.number_input(
        "**$-Duration**", 
        value=810, 
        help="Measures raw dollar price sensitivity. \n\n" \
        " Usually a negative number because prices move inversely to yields."
    )

with col5:
    convexity = st.number_input(
        "**$-Convexity**", 
        value=8500, 
        help="Measures the curvature of the bond price.\n\n" \
        "Adds accuracy for large rate shifts by correcting the straight line duration estimate."
    )



col_dir, col_mag = st.columns(2, border=True)

with col_dir:
    rate_direction = st.radio(
        "**Interest Rate Shift**", 
        ["Increase", "Decrease"], 
        help="Select whether the central bank is hiking (Increase) or cutting (Decrease) rates."
    )

with col_mag:
    
    magnitude_bps = st.number_input(
        "**Magnitude Change (Basis Points)**", 
        value=50, 
        help="100 bps = 1%, 50 = 0.5% shift."
    )



dr_magnitude = magnitude_bps / 10000
dr = dr_magnitude if rate_direction == "Increase" else -dr_magnitude

    
    
r_c , foa, soa = get_bond_sensitivity(m_d, dr,d_d,convexity)

st.divider()

res_col1, res_col2, res_col3 = st.columns(3, border=True)
    

with res_col1:
        st.metric(
            label="Relative Price Change", 
            value=f"{r_c * 100:.2f}%", 
            help="The percentage change on bond's value."
        )


with res_col2:
        st.metric(
            label="Linear Price Change", 
            value=f"{'-' if foa < 0 else ''}${abs(foa):,.2f}",
            help=" The first-order approximation (assumes a straight line)."
        )


with res_col3:
        st.metric(
            label="True Price Change", 
            value=f"{'-' if soa < 0 else ''}${abs(soa):.2f}", 
            help="The second-order approximation accounting for curvature."
        )
        
    

st.subheader("Interpretation")
    
if dr > 0:
        st.error(
            f"**As the rates went UP, the bond value went DOWN.**\n\n"
            f"A **{magnitude_bps} bps** change indicates a price drop of about **${abs(soa):.2f}**\n\n "
            f"Because bond prices have a natural curve to them, this drop isn't quite as bad as a basic straight-line estimate would predict."
        )


elif dr < 0:
        st.success(
            f"**As the rates went DOWN, the bond value went UP.**\n\n"
            f"A **{magnitude_bps} bps** change indicates a price increase of about **${soa:.2f}** \n\n "
            f"Due to the natural curve of bond prices, the actual profit is slightly larger than a basic straight-line estimate would predict."
        )

else:
        st.info("**Rates stayed the same.** \n\n bond price hasn't moved based on interest rates.")