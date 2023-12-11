input = open('./input_11.txt', 'r')
lines = input.readlines()
L = [list(line.strip()) for line in lines]
m = len(L)
n = len(L[0])
empty_rows = [True for _ in range(m)]
empty_cols = [True for _ in range(n)]

for i in range(m):
    for j in range(n):
        if L[i][j] == '#':
            empty_rows[i] = False
            empty_cols[j] = False

row_add = [0 for _ in range(m+1)]
col_add = [0 for _ in range(n+1)]

addition = 1

for k, v in enumerate(empty_rows):
    row_add[k+1] = row_add[k]
    if v:
        row_add[k+1] += addition
row_add.pop(0)

for k, v in enumerate(empty_cols):
    col_add[k+1] = col_add[k]
    if v:
        col_add[k+1] += addition
col_add.pop(0)

G = []
cnt_G = 0
for i in range(m):
    for j in range(n):
        if L[i][j] == '#':
            L[i][j] = cnt_G
            G.append((i+row_add[i], j+col_add[j]))
            cnt_G += 1

res = 0
for i in range(cnt_G):
    for j in range(i+1, cnt_G):
        x, y = G[i]
        u, v = G[j]
        res += (abs(y - v) + abs(x - u))
print(res)