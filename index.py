import streamlit as st
import yfinance as yf
import numpy as np
from scipy.stats import norm

# Black-Scholes Option Pricing Formula
def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return option_price

# Get stock data
def get_stock_data(ticker):
    stock_data = yf.download(ticker, period="1y", interval="1d")
    close = stock_data['Close']
    # yfinance may return multi-level columns; flatten to a simple Series
    if hasattr(close, 'columns'):
        close = close.iloc[:, 0]
    return close

# Calculate volatility
def calculate_volatility(stock_prices):
    returns = np.log(stock_prices / stock_prices.shift(1))
    volatility = float(np.std(returns) * np.sqrt(252))  # Annualize volatility
    return volatility

# Streamlit Web Interface
st.title("Real-Time Option Pricing with Black-Scholes")



# Input form
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
strike_price = st.number_input("Enter Strike Price:", min_value=1.0, value=150.0)
time_to_maturity = st.number_input("Enter Time to Maturity (in years):", min_value=0.01, value=0.5)
risk_free_rate = st.number_input("Enter Risk-Free Rate (as decimal):", min_value=0.0, max_value=1.0, value=0.05)
option_type = st.selectbox("Select Option Type:", ("call", "put"))

# Get stock data
stock_prices = get_stock_data(ticker)
current_price = float(stock_prices.iloc[-1])
volatility = calculate_volatility(stock_prices)

# Black-Scholes calculation
bs_price = black_scholes(current_price, strike_price, time_to_maturity, risk_free_rate, volatility, option_type)

# Values are already scalars
stock_ticker = ticker.upper()
current_stock_price = current_price
volatility_value = volatility
option_value = bs_price


# Display results with proper formatting and custom CSS
st.markdown("""
    <style>
        .result-container {
            font-family: Arial, sans-serif;
            margin: 20px 0;
            padding: 10px;
            border: 2px solid #2C3E50;
            border-radius: 8px;
            background-color: #f1f1f1;
        }
        .result-title {
            font-size: 18px;
            font-weight: bold;
            color: #2C3E50;
        }
        .result-value {
            font-size: 16px;
            color: #16A085;
        }
        .result-row {
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Display the results
st.markdown(f"""
    <div class="result-container">
        <div class="result-row">
            <div class="result-title">Ticker: {stock_ticker}</div>
            <div class="result-value">Current Stock Price: ${current_stock_price:.2f}</div>
        </div>
        <div class="result-row">
            <div class="result-title">Annualized Volatility</div>
            <div class="result-value">Volatility: {volatility_value:.6f} ({volatility_value*100:.2f}%)</div>
        </div>
        <div class="result-row">
            <div class="result-title">Black-Scholes Result</div>
            <div class="result-value">Option Price ({option_type.capitalize()}): ${option_value:.4f}</div>
        </div>
    </div>
""", unsafe_allow_html=True)
