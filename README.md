### **Option Pricer Project Description**

The **Option Pricer** is an interactive web-based application built in Python that allows users to calculate the theoretical prices of European call and put options using the Black-Scholes model. Designed to be user-friendly and efficient, the project leverages real-time market data and financial modeling principles to deliver accurate and actionable insights.


### **Key Features**
1. **Real-Time Stock Price Integration:**
   - Uses the `yfinance` library to fetch live stock prices, ensuring calculations are based on the latest market data.

2. **Black-Scholes Model Implementation:**
   - Accurately calculates option prices for European-style options using standard financial formulas.
   - Supports both call and put options.

3. **Interactive Web Interface:**
   - Built with `Dash`, the app provides a sleek and intuitive interface where users can:
     - Input stock ticker symbols, strike prices, time to expiration, risk-free rates, volatility, and option type.
     - Trigger option price calculations with the click of a button.
   - Results are displayed dynamically, with error handling for invalid inputs or issues fetching data.

4. **Customizable Inputs:**
   - Allows users to test different scenarios by adjusting variables like volatility, strike price, and time to maturity.

5. **Error Handling:**
   - Handles invalid inputs and provides clear error messages to guide the user.



### **Technologies Used**
- **Python:** Core language for logic and implementation.
- **Dash:** Framework for building the interactive web application.
- **Numpy & Scipy:** Libraries for mathematical and statistical computations.
- **YFinance:** For fetching real-time stock price data.

