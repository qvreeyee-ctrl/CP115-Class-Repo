speed = int(input())
total_readings = 0
longest_streak = 0
streak = 0 

while speed >= 0 :
    total_readings += speed
    if speed < 20 :
        streak = speed 
        streak += speed
        if speed > streak :
            longest_streak = streak

speed = int(input())

print(total_readings)
print(longest_streak)
