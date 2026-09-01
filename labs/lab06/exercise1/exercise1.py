# Exercise 13: Student Card

# Ask for user input
full_name = input("Enter your full name: ")
matric_number = input("Enter your matric number: ")

# Process the data
uppercase_name = full_name.upper()
name_length = len(full_name)

# Display results
print(f"Name in uppercase: {uppercase_name}")
print(f"Number of characters in name: {name_length}")
print(f"Matric number: {matric_number}")