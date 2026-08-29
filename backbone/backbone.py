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

"""print("Start:", total_value(cash, shares, price=50.0))   # 1000.0

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
"""

prices = [50.0, 51.0, 49.0, 48.0, 52.0, 55.0, 54.0, 53.0, 57.0, 60.0]
readable_prices = []

print("MOMENTUM STRATEGY")
for today_index in range(len(prices)):
    today_price = prices[today_index]

    if len(readable_prices) > 0:
        average = sum(readable_prices) / len(readable_prices)


        if today_price > average and shares == 0: #price above normal so buy
            cash, shares = buy_shares(cash, shares, today_price, quantity = 10)
            print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: " + str(average) + " | BOUGHT 10 shares at " + str(today_price))

        elif today_price < average and shares > 0: #price below normal so sell
            cash, shares = sell_shares(cash, shares, today_price, quantity = 10)
            print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: " + str(average) + " | SOLD 10 shares at " + str(today_price))
        average = sum(readable_prices) / len(readable_prices)
        print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: " + str(average))

    else:
        print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: N/A")

    readable_prices.append(today_price)

print (f"End: cash = " + str(cash) + " | shares = " + str(shares) + " | total worth = " + str(total_value(cash, shares, today_price)))
print("\n\n")

readable_prices = []
cash = 1000.0
shares = 0

print("MEAN REVERSION STRATEGY")
for today_index in range(len(prices)):
    today_price = prices[today_index]

    if len(readable_prices) > 0:
        average = sum(readable_prices) / len(readable_prices)

        if today_price < average and shares == 0: #price below normal so buy
            cash, shares = buy_shares(cash, shares, today_price, quantity = 10)
            print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: " + str(average) + " | BOUGHT 10 shares at " + str(today_price))

        elif today_price > average and shares > 0: #price above normal so sell
            cash, shares = sell_shares(cash, shares, today_price, quantity = 10)
            print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: " + str(average) + " | SOLD 10 shares at " + str(today_price))
        average = sum(readable_prices) / len(readable_prices)
        print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: " + str(average))

    else:
        print(f"Day " + str(today_index) + " price: " + str(today_price) + " | past average: N/A")

    readable_prices.append(today_price)
print (f"End: cash = " + str(cash) + " | shares = " + str(shares) + " | total worth = " + str(total_value(cash, shares, today_price)))