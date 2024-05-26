from lib.testing import cash_register_test


class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.transactions = []
        self.last_transaction = 0
        self.discount = discount

    def add_item(self, item):
        self.transactions.append(item)
        self.total += item
        self.last_transaction = item

    def apply_discount(self):
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

    def void_last_transaction(self):
        if self.transactions:
            self.total -= self.last_transaction
            self.transactions.pop()
            self.last_transaction = self.transactions[-1] if self.transactions else 0

    def get_total(self):
        return self.total
    
    cash_register_with_discount = cash_register_test(discount=20)
# Create a CashRegister instance with a 20% discount
cash_register_with_discount = CashRegister(discount=20)

# Add some items
cash_register_with_discount.add_item(10)
cash_register_with_discount.add_item(20)
cash_register_with_discount.add_item(30)

# Apply the discount
cash_register_with_discount.apply_discount()

# Print the total amount after applying the discount
print(cash_register_with_discount.get_total())