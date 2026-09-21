main_course = input()
drink = input()
dessert = input()

# Prices
if main_course == "Chicken":
    main_price = 10
elif main_course == "Beef":
    main_price = 12
elif main_course == "Fish":
    main_price = 11

if drink == "Soft Drink":
    drink_price = 2
elif drink == "Coffee":
    drink_price = 3

if dessert == "Ice Cream":
    dessert_price = 4
elif dessert == "Cake":
    dessert_price = 5

food_cost = main_price + drink_price + dessert_price
final_bill = food_cost + (food_cost * 0.10)

print(f"{final_bill:.2f}")