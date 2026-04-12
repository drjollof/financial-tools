import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title('Merton Model Simulator')

st.markdown("""
*Evaluate credit risk and housing debt by treating equity as a call option on underlying property assets. 
Simulate Default Zones in non-recourse loans to determine when a borrower might rationally choose to walk away from debt in a volatile market*
""")
st.divider()

def plot_merton_model(asset_value, debt_value, volatility, time_to_expiry):
   

    t = np.linspace(0, time_to_expiry, 100)
    dt = time_to_expiry / 100
    
    
    
    np.random.seed(42)  
    shocks = np.random.normal(0, asset_value * (volatility/100), 100)
    asset_path = asset_value + np.cumsum(shocks)
    
   
    fig, ax = plt.subplots(figsize=(10, 5), dpi = 100)
    
    

    ax.axhline(debt_value, color='#ff4b4b', linestyle='--', label="Debt Floor (Mortgage)")
    ax.plot(t, asset_path, color='#007bff', linewidth=2, label="Asset Value (Home)")
    
    ax.fill_between(t, asset_path, debt_value, 
                    where=(asset_path < debt_value), 
                    color='red', alpha=0.3, label="Default Zone")
    
    

    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    ax.tick_params(colors='white')

   

    ax.set_xlabel("Time (Years)", color='white')
    ax.set_ylabel("Value ($)", color='white')
    ax.legend(facecolor='#0e1117', edgecolor='none', labelcolor='white', )
    
    return fig

col1, col2 = st.columns(2, border=True)

with col1:
    a_v = st.number_input('**Home/Asset Value ($)**', value=0)
    d_v = st.number_input('**Mortgage/Debt Value ($)**', value = 0)
    

with col2:
    t = st.number_input('**Time to Expiry (years)**', value= 0)
    vol = st.slider('**Volatility (%)**', min_value=0.0, 
                    max_value=50.0,
                    value=20.0,
                    step=1.0)

container = st.container(border=True)
container.write('**Merton Model Chart (Asset Value vs. Debt)**')
container.pyplot(plot_merton_model(a_v, d_v, vol, t))

def get_metrics(asset_value, debt, volatility):
    e_v = np.maximum(asset_value - debt, 0)
    o_v = np.maximum(debt - asset_value, 0)
    d_d = (asset_value - debt) / ((volatility/100) * asset_value) if asset_value > 0 else 0

    return e_v, o_v, d_d


col3, col4, col5 = st.columns(3, border=True)

E_V , O_V , D_D = get_metrics(a_v, d_v, vol)
with col3:
    st.metric('**Equity Value (Call)**', f'${E_V :.0f}')


with col4:
    st.metric('**Right to Default (Put)**', f'{O_V :.0f}')
             

with col5:
    st.metric('**Distance to Default**', f'{D_D :.2f}')

container = st.container(border=True)

if O_V > 0:
    container.warning('**UNDERWATER**')
else:
    container.success('**SAFE**')


glossary_data = {
    "Term": ["Asset Value", "Debt Value", "Equity", "Right to Default", "Volatility", "Default Zone"],
    "Derivative Concept": ["Underlying", "Strike Price", "Call Option", "Put Option", "Uncertainty", "ITM (Put)"],
    "Real-World Meaning": [
        "Market price of the property",
        "Total mortgage owed",
        "Your ownership stake (max(A-D, 0))",
        "The right to walk away from a bad loan",
        "Frequency of price swings",
        "When the house is 'underwater'"
    ]
}

st.divider()
st.subheader("Merton Model Glossary")
st.table(pd.DataFrame(glossary_data))







st.markdown("---")
st.caption("""
This application is strictly for **educational purposes only**. 
The calculations and data provided do not constitute professional financial advice or a real-world financial tool. 
""")