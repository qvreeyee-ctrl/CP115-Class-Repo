import math

radius =float(input("Enter radius : "))

area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

print(f"Circumference : {circumference}")
print(f"Area : {area}")