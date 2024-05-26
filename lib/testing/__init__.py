class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.transactions = []
        self.last_transaction = 0
        self.discount = discount
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