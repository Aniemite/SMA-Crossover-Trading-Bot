class MockTradingAPI:
    def __init__(self, balance):
        self._balance = balance

    def place_order(self, trade, price):
        if trade.signal == "Buy":
            cost = trade.amount * price
            if self._balance >= cost:
                self._balance -= cost
                print(f"[BROKER] BUY @ {price:.2f} | Balance: {self._balance:.2f}")
            else:
                print("[BROKER] Insufficient balance")

        elif trade.signal == "Sell":
            self._balance += trade.amount * price
            print(f"[BROKER] SELL @ {price:.2f} | Balance: {self._balance:.2f}")

    @property
    def balance(self):
        return self._balance