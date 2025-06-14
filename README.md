# 📊 Portfolio Optimizer App

A **Streamlit-based Portfolio Optimization App** using Monte Carlo simulation to help investors find the optimal asset allocation with the maximum Sharpe Ratio.  
This app provides a modern, interactive, and mobile-friendly interface.

---

## 🚀 Key Features
- 📥 Upload your own **Excel file** with historical stock prices.
- ⚙️ Customize the **Risk-Free Rate (%)** and **Number of Simulations**.
- 🔍 Real-time calculation of:
  - Daily returns
  - Optimal portfolio weights
  - Expected annual return
  - Annualized risk (volatility)
  - Sharpe Ratio
- 📊 Visualize the **Efficient Frontier** with the optimal portfolio highlighted.
- 📱 Mobile and desktop responsive.
- 🌟 Can be installed as a **Progressive Web App (PWA)** shortcut on your home screen.

---

## 📂 How to Use

### 1️⃣ Open the App  
👉 **[Launch the App Here](https://portfolio-optimizer-dbel3qn7uxpxhrdaqipz6s.streamlit.app/)**  

*(Replace this link with your actual Streamlit Cloud deployment URL)*

---

### 2️⃣ Prepare Your Excel File  
Your Excel file should look like this:

| Date       | Stock1 | Stock2 | Stock3 |
|------------|--------|--------|--------|
| 2024-01-01 | 100.00 | 50.00  | 75.00  |
| 2024-01-02 | 101.00 | 51.00  | 74.00  |
| 2024-01-03 | 102.00 | 52.00  | 76.00  |

✔️ **Guidelines:**  
- The first column must be named **`Date`**.  
- Data can be sorted **oldest to newest** or **newest to oldest**; the app will automatically sort it correctly.  
- Each other column should represent stock prices.

---

### 3️⃣ Run the Simulation  
- 📤 Upload your Excel file in the app.  
- 🛠️ Adjust **Risk-Free Rate** and **Number of Portfolios (Simulations)** using the sidebar.  
- 📈 See:  
  - Daily returns (sample displayed)  
  - Optimal portfolio weights  
  - Portfolio performance (return, risk, Sharpe Ratio)  
  - Efficient frontier chart  

---

### 4️⃣ Mobile Setup (PWA Style)  
- Open the app in your **mobile browser**.  
- Select **"Add to Home Screen"** from browser options.  
- The app will now behave like a **native mobile app** with your custom name and icon (browser-dependent, full PWA support is limited in Streamlit).

---

## 📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## 📬 Contact

Created by [hesha11] — [k.w.heshannimsara2003@gmail.com]  
Feel free to contribute or report issues on GitHub.

