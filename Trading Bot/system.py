import yfinance as yf
from trade import MyTrade


class MyTradingSystem:
    def __init__(self, api, strategy, symbol):
        self.api = api
        self.strategy = strategy
        self.symbol = symbol
        self.price_data = []

    def fetch_price(self):
        data = yf.download(
            tickers=self.symbol,
            period="1d",
            interval="1m",
            progress=False
        )

        if not data.empty:
            price = float(data["Close"].iloc[-1])
            self.price_data.append(price)

            if len(self.price_data) > self.strategy.lwindow:
                self.price_data.pop(0)

            print(f"[DATA] Latest Price: {price:.2f}")
            return price
        return None

    def run(self):
        price = self.fetch_price()
        if price is None:
            return

        signal = self.strategy.generate_signal(self.price_data)
        print(f"[SIGNAL] {signal}")

        if signal in ("Buy", "Sell"):
            trade = MyTrade(self.strategy.name, signal, amount=1)
            trade.execute()
            self.api.place_order(trade, price)