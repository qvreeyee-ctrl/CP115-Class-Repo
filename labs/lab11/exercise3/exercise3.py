number = int(input())
biggest_jump = 0
prev_num = number
count = 0

while number != 0 :
    count += 1
    if prev_num > number:
        biggest_jump = number
    number = int(input())

print(count)
print(biggest_jump)
