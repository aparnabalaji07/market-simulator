cash = 1000.0
shares = 0
price = 50.0

def buy_shares(cash, shares, price, quantity):
    cost = price * quantity
    cash = cash - cost
    shares = shares + quantity
    return cash, shares

def sell_shares(cash, shares, price, quantity):
    revenue = price * quantity
    cash = cash + revenue
    shares = shares - quantity
    return cash, shares

def total_value(cash, shares, price):
    return cash + (shares * price)



cash = 1000.0
shares = 0

print("Start:", total_value(cash, shares, price=50.0))   # 1000.0

cash, shares = buy_shares(cash, shares, price=50.0, quantity=10)
print("After buying 10 at $50:")
print("  cash: ", cash, "| shares: ", shares)
print("  worth: ", total_value(cash, shares, price=50.0))

print("Price rises to $55, worth now: ", total_value(cash, shares, price=55.0))

cash, shares = sell_shares(cash, shares, price=55.0, quantity=10)
print("After selling 10 at $55: ")
print("  cash: ", cash, "| shares: ", shares)
print("  worth: ", total_value(cash, shares, price=55.0))

cash = 1000.0
shares = 0

print("Start: ", total_value(cash, shares, price=50.0))   # 1000.0

cash, shares = buy_shares(cash, shares, price=50.0, quantity=10)
print("After buying 10 at $50:")
print("  cash: ", cash, "| shares: ", shares)
print("  worth: ", total_value(cash, shares, price=50.0))

print("Price drops to $45, worth now: ", total_value(cash, shares, price=45.0))

cash, shares = sell_shares(cash, shares, price=45.0, quantity=10)
print("After selling 10 at $45: ")
print("  cash: ", cash, "| shares: ", shares)
print("  worth: ", total_value(cash, shares, price=45.0))