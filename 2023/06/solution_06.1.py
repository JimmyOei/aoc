input = open('./input_06.txt', 'r')
lines = input.readlines()

times = [int(num) for num in lines[0].split() if num.isdigit()]
dists = [int(num) for num in lines[1].split() if num.isdigit()]
n = len(times)

res = 1
for i in range(n):
    t = times[i]
    d = dists[i]
    wins = 0
    for k in range(t+1//2):
        if d < (t-k)*k:
            wins += 1
    res *= wins
print(res)