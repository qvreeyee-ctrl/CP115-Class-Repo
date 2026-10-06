number = int(input())
score = 0
ignored = 0
current_score = 0

while number != 0 :
    if number > current_score :
        current_score = number
        score += current_score
        
    else :
        ignored += 1

    number = int(input())

print(score)
print(ignored)
