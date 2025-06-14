# 📥 Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 🎨 Streamlit Page Setup
st.set_page_config(page_title='🌟 Supreme Portfolio Optimizer', layout='wide')

# 🎯 App Header
st.title("💼 Supreme Portfolio Optimizer")
st.write("""
Upload your portfolio Excel file with **historical prices** (Date in the first column, then stock prices).
This app finds the **optimal portfolio** by maximizing the Sharpe Ratio 🚀.
""")

# 📤 File Uploader
uploaded_file = st.file_uploader("📂 Upload Excel file", type=['xlsx'])

# 🎛️ Sidebar Settings
st.sidebar.header("⚙️ Simulation Settings")
risk_free_rate = st.sidebar.number_input('Risk-Free Rate (%)', min_value=0.0, max_value=10.0, value=2.0, step=0.1) / 100
num_portfolios = st.sidebar.number_input('Number of Simulated Portfolios', min_value=1000, max_value=50000, value=10000, step=1000)

if uploaded_file is not None:
    try:
        # 🔄 Load and Prepare Data
        df = pd.read_excel(uploaded_file)
        df['Date'] = pd.to_datetime(df['Date'])
        df.sort_values('Date', inplace=True)
        df.set_index('Date', inplace=True)

        st.subheader("📅 Price Data (First 5 Rows)")
        st.dataframe(df.head())

        # 📈 Calculate Daily Returns
        returns = df.pct_change().dropna()
        st.subheader("📈 Daily Returns (First 5 Rows)")
        st.dataframe(returns.head())

        # 📊 Calculate Annualized Expected Returns and Covariance Matrix
        expected_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252

        # 🎲 Monte Carlo Simulation
        num_assets = len(df.columns)
        results = np.zeros((3, num_portfolios))
        weights_record = []

        np.random.seed(42)
        for i in range(num_portfolios):
            weights = np.random.random(num_assets)
            weights /= np.sum(weights)
            weights_record.append(weights)

            portfolio_return = np.sum(weights * expected_returns)
            portfolio_stddev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            sharpe_ratio = portfolio_return / portfolio_stddev  # Risk-free rate is ignored for weights

            results[0, i] = portfolio_return
            results[1, i] = portfolio_stddev
            results[2, i] = sharpe_ratio

        # 📌 Prepare Results
        results_df = pd.DataFrame(results.T, columns=['Return', 'Risk', 'Sharpe'])
        max_sharpe_idx = results_df['Sharpe'].idxmax()
        optimal_weights = weights_record[max_sharpe_idx]

        # 🚩 Calculate Sharpe Ratio with User's Risk-Free Rate (Correct Calculation)
        results_df['Sharpe_Adjusted'] = (results_df['Return'] - risk_free_rate) / results_df['Risk']

        # 🔍 Optimal Portfolio Details
        st.subheader("🔍 Optimal Portfolio Weights")
        opt_df = pd.DataFrame({
            "Stock": df.columns,
            "Weight": [f"{w:.2%}" for w in optimal_weights]
        })
        st.table(opt_df)

        opt_return = results_df.loc[max_sharpe_idx, 'Return']
        opt_risk = results_df.loc[max_sharpe_idx, 'Risk']
        opt_sharpe_adjusted = (opt_return - risk_free_rate) / opt_risk

        # 📊 Portfolio Performance
        st.subheader("📈 Portfolio Performance")
        st.write(f"**Expected Annual Return:** {opt_return:.2%}")
        st.write(f"**Annual Risk (Volatility):** {opt_risk:.2%}")
        st.write(f"**Sharpe Ratio (Adjusted for Risk-Free Rate):** {opt_sharpe_adjusted:.2f}")

        # 🎨 Plot Efficient Frontier
        st.subheader("🌐 Efficient Frontier (Sharpe Ratio Adjusted)")
        fig, ax = plt.subplots(figsize=(12, 8))
        scatter = ax.scatter(results_df['Risk'], results_df['Return'], c=results_df['Sharpe_Adjusted'], cmap='plasma')
        ax.scatter(opt_risk, opt_return, color='red', marker='*', s=500, label='Optimal Portfolio')
        ax.set_xlabel('Risk (Standard Deviation)')
        ax.set_ylabel('Expected Return')
        ax.set_title('Efficient Frontier (Sharpe Ratio Adjusted)')
        ax.legend()
        fig.colorbar(scatter, label='Sharpe Ratio (Adjusted)')

        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")

else:
    st.info("👈 Please upload your portfolio Excel file to start optimization.")
