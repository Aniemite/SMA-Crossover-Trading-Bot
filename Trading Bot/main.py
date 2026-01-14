import time
from broker import MockTradingAPI
from strategy import MySmaTradingStrategy
from system import MyTradingSystem

SYMBOL = "AAPL"

api = MockTradingAPI(balance=10_000)
strategy = MySmaTradingStrategy(swindow=3, lwindow=5)
system = MyTradingSystem(api, strategy, SYMBOL)

while True:
    system.run()
    print(f"[BALANCE] {api.balance:.2f}")
    time.sleep(3)