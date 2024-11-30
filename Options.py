#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import norm
import yfinance as yf
from dash import Dash, dcc, html, Input, Output

# Function to calculate Black-Scholes option prices
def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Black-Scholes price for European options.

    Parameters:
    S : float - Current stock price
    K : float - Strike price
    T : float - Time to expiration in years
    r : float - Risk-free interest rate
    sigma : float - Volatility of the stock
    option_type : str - 'call' or 'put'

    Returns:
    float - Theoretical price of the option
    """
    d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    return price

# Dash app setup
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Option Pricer", style={"textAlign": "center"}),

    html.Label("Stock Ticker:"),
    dcc.Input(id="stock-ticker", type="text", placeholder="e.g., AAPL", value="AAPL"),

    html.Label("Strike Price (K):"),
    dcc.Input(id="strike-price", type="number", placeholder="e.g., 110", value=110),

    html.Label("Time to Expiration (T in years):"),
    dcc.Input(id="time-expiration", type="number", placeholder="e.g., 1", value=1),

    html.Label("Risk-Free Rate (r):"),
    dcc.Input(id="risk-free-rate", type="number", placeholder="e.g., 0.05", value=0.05),

    html.Label("Volatility (sigma):"),
    dcc.Input(id="volatility", type="number", placeholder="e.g., 0.2", value=0.2),

    html.Label("Option Type:"),
    dcc.Dropdown(
        id="option-type",
        options=[
            {"label": "Call", "value": "call"},
            {"label": "Put", "value": "put"}
        ],
        value="call"
    ),

    html.Button("Calculate", id="calculate-button", n_clicks=0),

    html.H2(id="output-price", style={"textAlign": "center"})
])

# Callback to calculate and display the option price
@app.callback(
    Output("output-price", "children"),
    [
        Input("stock-ticker", "value"),
        Input("strike-price", "value"),
        Input("time-expiration", "value"),
        Input("risk-free-rate", "value"),
        Input("volatility", "value"),
        Input("option-type", "value"),
        Input("calculate-button", "n_clicks")
    ]
)
def update_option_price(stock_ticker, K, T, r, sigma, option_type, n_clicks):
    if n_clicks > 0:
        # Fetch current stock price
        stock = yf.Ticker(stock_ticker)
        try:
            S = stock.history(period="1d")['Close'][-1]
        except Exception as e:
            return f"Error fetching stock price: {e}"

        # Calculate option price
        try:
            price = black_scholes(S, K, T, r, sigma, option_type)
            return f"The {option_type.capitalize()} Option Price is: ${price:.2f}"
        except Exception as e:
            return f"Error calculating option price: {e}"

    return "Enter values and press Calculate."

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)


# In[ ]:




