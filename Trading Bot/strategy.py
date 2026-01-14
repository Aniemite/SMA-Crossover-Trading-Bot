class MyTradingStrategy:
    def __init__(self, name):
        self._name = name

    def generate_signal(self, price_data):
        raise NotImplementedError("generate_signal must be implemented")

    @property
    def name(self):
        return self._name


class MySmaTradingStrategy(MyTradingStrategy):
    def __init__(self, swindow, lwindow):
        super().__init__("SMA Crossover Strategy")
        self._swindow = swindow
        self._lwindow = lwindow

    def generate_signal(self, price_data):
        if len(price_data) < self._lwindow:
            return "Hold"

        short_avg = sum(price_data[-self._swindow:]) / self._swindow
        long_avg = sum(price_data[-self._lwindow:]) / self._lwindow

        if short_avg > long_avg:
            return "Buy"
        elif short_avg < long_avg:
            return "Sell"
        return "Hold"

    @property
    def lwindow(self):
        return self._lwindow