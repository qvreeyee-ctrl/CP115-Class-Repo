speed = int(input())

total_readings = 0
longest_streak = 0 
current_speed = 0

while speed >= 0 :
    total_readings += 1

    if speed < 20 :
        current_speed += 1
        if current_speed > longest_streak:
            longest_streak += 1
    else:
        current_speed = 0
    
    speed = int(input())

print(total_readings)
print(longest_streak)
