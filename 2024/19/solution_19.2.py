input = open('./input_19.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

patterns = []
towels = []

idx = 0
for line in lines:
    if line == '\n' or line == '':
        break
    ps = line.split(', ')
    for p in ps:
      patterns.append(p)
    idx += 1

for line in lines[idx+1:]:
    towels.append(line)
    
memo = {}
def composable(towel):
    if towel in memo:
        return memo[towel]
      
    n = len(towel)
    if n == 0:
        return True
      
    memo[towel] = 0
    for p in patterns:
        m = len(p)
        if m > n:
            continue
        if towel[:m] == p:
            memo[towel] += composable(towel[m:])
    return memo[towel]

ans = 0
for towel in towels:
    ans += composable(towel)

print(ans)