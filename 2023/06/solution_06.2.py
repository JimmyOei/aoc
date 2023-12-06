input = open('./input_06.txt', 'r')
lines = input.readlines()

time = int(''.join(filter(str.isdigit, lines[0])))
dist = int(''.join(filter(str.isdigit, lines[1])))

print(time, dist)

wins = 0
for k in range(time+1//2):
    if dist < (time-k)*k:
        wins += 1
print(wins)