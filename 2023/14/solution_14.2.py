input = open('./input_14.txt', 'r')
lines = input.readlines()
L = [list(line.strip()) for line in lines]
m = len(L)
n = len(L[0])

def perform_cycle(G):
    top = [0] * n
    for i in range(m):
        for j in range(n):
            if G[i][j] == 'O':
                G[i][j] = '.'
                G[top[j]][j] = 'O'
                top[j] += 1
            elif G[i][j] == '#':
                top[j] = i+1

    left = [0] * m
    for j in range(n):
        for i in range(m):
            if G[i][j] == 'O':
                G[i][j] = '.'
                G[i][left[i]] = 'O'
                left[i] += 1
            elif G[i][j] == '#':
                left[i] = j+1

    bot = [m-1] * n
    for i in reversed(range(m)):
        for j in range(n):
            if G[i][j] == 'O':
                G[i][j] = '.'
                G[bot[j]][j] = 'O'
                bot[j] -= 1
            elif G[i][j] == '#':
                bot[j] = i-1

    right = [n-1] * m
    for j in reversed(range(n)):
        for i in range(m):
            if G[i][j] == 'O':
                G[i][j] = '.'
                G[i][right[i]] = 'O'
                right[i] -= 1
            elif G[i][j] == '#':
                right[i] = j-1
    return G


CYCLES = 1000000000
seen = {}
G = L.copy()

for c in range(CYCLES):
    h = hash(str(G))
    if h in seen:
        ch = seen[h]
        cycles_left = (CYCLES - ch) % (c - ch)
        for _ in range(cycles_left):
            G = perform_cycle(G)
        break
    
    seen[h] = c
    G = perform_cycle(G)

res = 0
for i, row in enumerate(G):
    res += (m-i)*row.count('O')
print(res)
