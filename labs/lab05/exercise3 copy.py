import random

name = input("Enter student name: ")
print(name)
random_number = random.randint(1, 10)
print("Random number: {random_number}")

print ("{}{}".format("Class information ;  Name: " + name, "       Random number: " + str(random_number)))