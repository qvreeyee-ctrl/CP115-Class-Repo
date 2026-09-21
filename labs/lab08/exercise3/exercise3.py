day_type = input()
show_time = int(input())
customer_type = input()

# Tentukan base price
if day_type == "weekend":
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15
else:  # Weekday
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12

# Tentukan final price
if show_time > 18:
    final_price = base_price + 3
else:
    final_price = base_price

# Output
print(base_price)
print(final_price)