print("name=pushpa,usn=1AY24AI086,section=)")
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    flips = [random.randint(0, 1) for _ in range(100)]
    streak = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                break  
        else:
            streak = 1

print(f'Chance of streak:{numberOfStreaks/100}%')