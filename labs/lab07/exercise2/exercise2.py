amount = int(input())

# calculating number of rm50 notes and remaining coins
notes = amount // 50
coins = amount % 50
print(notes)
print(coins)