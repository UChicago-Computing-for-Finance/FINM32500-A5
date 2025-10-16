class Broker:
    def __init__(self, cash: float = 1_000_000):
        self.cash = cash
        self.position = 0

    def market_order(self, side: str, qty: int, price: float):

        if side == "BUY" and self.cash >= qty * price:
            self.cash -= qty * price
            self.position += 1
        if side == "SELL" and self.position >= 1:
            self.cash += qty * price
            self.position -= 1