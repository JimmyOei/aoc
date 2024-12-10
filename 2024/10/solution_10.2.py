input = open('./input_10.txt', 'r')
lines = input.readlines()
lines = [list(line.strip()) for line in lines]
lines = [[int(c) for c in line] for line in lines]

s = []
n = len(lines)
m = len(lines[0])

for i in range(n):
    for j in range(m):
        if lines[i][j] == 0:
            s.append((i, j, 0))

ans = 0
for si in s:
    st = [si]
    while len(st) > 0:
        i, j, v = st.pop()
        if v == 9:
            ans += 1
            continue
        if i+1 < n and lines[i+1][j] == v+1:
            st.append((i+1, j, v+1))
        if i-1 >= 0 and lines[i-1][j] == v+1:
            st.append((i-1, j, v+1))
        if j+1 < m and lines[i][j+1] == v+1:
            st.append((i, j+1, v+1))
        if j-1 >= 0 and lines[i][j-1] == v+1:
            st.append((i, j-1, v+1))

print(ans)