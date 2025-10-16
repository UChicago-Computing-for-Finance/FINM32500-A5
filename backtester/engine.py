import pandas as pd

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series):

        signals = self.strategy.signals(prices)

        for timestamp, signal in signals.items():
            if signal == 1:
                self.broker.market_order("BUY", 1, prices[timestamp])
            elif signal == -1:
                self.broker.market_order("SELL", 1, prices[timestamp])
            else:
                pass