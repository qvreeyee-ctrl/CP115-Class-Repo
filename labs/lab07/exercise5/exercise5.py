name = input()
password = input()
origin = input()
destination = input()

username = name.lower()
name_length = len(name)
long_enough = len(password) >= 8
route = origin.upper() + "-" + destination.upper()

print(username)
print(name_length)
print(long_enough)
print(route)
