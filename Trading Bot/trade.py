from datetime import datetime


class MyTrade:
    def __init__(self, strategy_name, signal, amount):
        self.strategy_name = strategy_name
        self.signal = signal
        self.amount = amount
        self.timestamp = datetime.now()

    def execute(self):
        print(
            f"[TRADE] {self.signal} | Strategy: {self.strategy_name} | "
            f"Qty: {self.amount} | Time: {self.timestamp}"
        )