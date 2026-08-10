item_name = input("Enter the item name: ") #take item name from user as input
item_price = float(input("Enter the item price: ")) #take item price from user as input

quantity1 = int(input("Enter the quantity: ")) #take quantity from user as input
quantity2 = int(input("Enter the quantity: ")) #take quantity from user as input
quantity3 = int(input("Enter the quantity: ")) #take quantity from user as input

tax_rate = 0.06 #define tax rate as 6%

subtotal = item_price * (quantity1 + quantity2 + quantity3) #calculate subtotal
tax_amount = subtotal * tax_rate #calculate tax amount
total_coast = subtotal + tax_amount #calculate total cost
