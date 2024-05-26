class CashRegister:
    def __init__(self):
        self.total = 0
        self.transactions = []
        self.last_transaction = 0

    def ring_up(self, item_price):
        self.transactions.append(item_price)
        self.total += item_price
        self.last_transaction = item_price

    def apply_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100) * self.total
        self.total -= discount_amount
        return self.total

    def void_last_transaction(self):
        if self.transactions:
            self.total -= self.last_transaction
            self.transactions.pop()
            self.last_transaction = self.transactions[-1] if self.transactions else 0