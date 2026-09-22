num_rounds = int(input())

final_score = 0
rounds_processed = 0
for score in range (num_rounds):

    scores =int(input())
    if scores > 100:
        final_score += scores+ (scores * 0.20)
    else:
        final_score += scores

    rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)