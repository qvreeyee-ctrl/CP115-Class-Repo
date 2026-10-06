correct_password = "python123"
login_successful = False
attempts_used = 0
max_attempts = 3


for attempt in range (max_attempts):
    password = input()
    attempts_used == attempt
    attempts_used += 1
    if password == correct_password:
        login_successful= True
        break

print(login_successful)
print(attempts_used)
