# Financial Tools

A comprehensive, interactive web application built with Streamlit for financial concepts demonstration, simulation, and education. This application simplifies complex financial concepts into easy-to-understand interactive modules, covering everything from basic bond pricing to options strategies and credit risk modeling.

## Live Demo
You can explore and interact with the fully deployed version of the application here:  
**[Financial Markets Demo](https://financial-markets-demo.streamlit.app/)**

##  Disclaimer
**This application is strictly for educational purposes only.** The calculations, models, and data provided do not constitute professional financial advice or a real-world financial tool.

## Features

The application is divided into six distinct educational modules:

### Module 1: Foundations & Macroeconomics
* **Bond Pricing:** Determine the market value of a bond based on current interest rates and maturity. Includes duration and convexity metrics to measure interest rate sensitivity.
* **Inflation:** Calculate the true growth of wealth by adjusting nominal gains for inflation to see actual purchasing power.
* **Short Selling:** Track the short selling cycle, including financing fees, dividend obligations, and margin call thresholds.
* **Central Bank Reserve:** Simulate the fractional reserve banking system, the deposit multiplier effect, and bank run stress tests.

### Module 2: Performance & Valuation
* **Returns:** Calculate and compare arithmetic and logarithmic returns, and evaluate the impact of dividend yields.
* **Valuation Models:** Estimate intrinsic stock value using the Gordon Growth Model (GGM) and the H-Model.
* **Sharpe-Ratio:** Evaluate risk-adjusted performance by measuring expected returns against a risk-free benchmark.

### Module 3: Portfolio Management
* **Portfolio Simulator:** Design a custom two-asset portfolio to see how correlation drives diversification and creates a "Risk Gap."
* **Portfolio Performance:** Audit portfolio efficiency using the Sharpe Ratio, Coefficient of Variation (CV), and Value at Risk (VaR).
* **ETF Evaluation:** Calculate the Net Asset Value (NAV) of an ETF and check for stale pricing arbitrage risks.

### Module 4: Derivatives & Advanced Models
* **Payoff Visualizer:** Visualize the profit and loss profiles (Hockey Stick payoff) of Call and Put options.
* **Put Call Parity:** Detect market mispricing and arbitrage opportunities by comparing a Fiduciary Call and a Protective Put.
* **Merton Model Simulator:** Evaluate credit risk and housing debt by treating equity as a call option on underlying property assets, visualizing the "Right to Default."

### Module 5: Credit & Lending
* **Loan Evaluator:** Simulate mortgage underwriting using Loan-to-Value (LTV) and Debt-to-Income (DTI) ratios.
* **MBS Simulator:** Test how a securitized mortgage pool (Mortgage-Backed Securities) absorbs credit losses from the bottom up across different risk tranches.
* **Credit Risk:** Calculate Expected Loss on specific loans and determine the Implied Probability of Default from public bond spreads.

### Module 6: Real Estate & Equity Markets
* **Leverage and Development:** Calculate a homeowner's net equity and leverage multiplier, or figure out a real estate developer's absolute break-even sale price based on hard and soft costs.
* **Equity Research:** Evaluate intrinsic value based on P/E, P/B, and PEG ratios.
* **Technical Analysis:** Track simple price momentum and use the Relative Strength Index (RSI) to spot overbought or oversold conditions.

##  Prerequisites

Ensure you have Python 3.12 or newer installed. The project relies on the following core libraries:
* `streamlit` (>= 1.52.2)
* `pandas` (>= 2.3.3)
* `matplotlib` (>= 3.10.8)
* `plotly` (>= 6.5.2)

##  Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/drjollof/financial-tools
    cd financial-tools
    ```

2.  **Set up a virtual environment (Recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    If you are using `pip`, you can install the dependencies defined in the project:
    ```bash
    pip install streamlit pandas matplotlib plotly
    ```
    *(Note: This project uses `pyproject.toml` and `uv.lock`, so you can also use modern package managers like `uv` or `pip install .`)*

## Usage

To run the application locally, navigate to the root directory of the project and run the following command:

```bash
streamlit run app.py