# 📈 SMA Crossover Automated Trading Bot

An automated Python trading bot that fetches live intraday market data from Yahoo Finance and generates Buy/Sell signals using a Simple Moving Average (SMA) crossover strategy.

This project is designed as a **learning and research tool** to explore algorithmic trading, financial markets and the world of Quant finance.

---

## Features

- Live market data fetching using Yahoo Finance (`yfinance`)
- Intraday **1-minute timeframe** over a **1-day window**
- Simple Moving Average crossover strategy (**3-period & 5-period**)
- Simulated order execution
- Real-time signal generation every 3 seconds (customizable)
- Flexible structure

---

## Strategy Overview

The bot uses a **Simple Moving Average (SMA) Crossover Strategy**:

- **Buy** → Short-term SMA crosses above long-term SMA  
- **Sell** → Short-term SMA crosses below long-term SMA  
- **Hold** → No crossover detected  

Current configuration:
- Short SMA: **3 periods**
- Long SMA: **5 periods**
- Timeframe: **1-minute candles**
- Data window: **1 day**

---
## Tech Stack

- **Python**
- **yfinance**
- **datetime**

---

## How to Run

### Clone the Repository
```
git clone https://github.com/<your-username>/sma-crossover-auto-trading-bot.git
cd sma-crossover-auto-trading-bot
```

### Create and Activate a Virtual Environment (Recommended)
```
python -m venv venv
```
Activate:
Windows:
```
venv\Scripts\activate
```
macOS / Linux:
```
source venv/bin/activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Configure the Bot
```
Open main.py and adjust parameters if needed:
```
```
SYMBOL = "AAPL"
strategy = MySmaTradingStrategy(swindow=3, lwindow=5)
api = MockTradingAPI(balance=10000)
```
### Run the Bot

```
python main.py
```
The system fetches new price data every 3 seconds and prints trading signals and simulated executions.

### Sample Output
```
[DATA] Latest Price: 189.42
[SIGNAL] Buy
[TRADE] Buy | Strategy: SMA Crossover Strategy | Qty: 1
[BROKER] BUY @ 189.42 | Balance: 9810.58
```
### Important Notes

This project uses Yahoo Finance, which may have rate limits.
Trades are simulated only using a mock broker.
This project is intended for educational and research purposes only.
It does not constitute financial advice.

### Stopping the Bot

Press:
 ```
CTRL + C
```
in the terminal to stop execution.

### Future Improvements

Historical backtesting module
Performance metrics (PnL, returns, drawdown)
Risk management (position sizing, stop-loss)
Multiple strategy support
Integration with real broker APIs (paper trading)

### Author

Harshvardhan Bablani
Aspiring Quant Developer | Python & C++ | Financial Markets


---
