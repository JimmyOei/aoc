input = open('./input_13.txt', 'r')
lines = input.readlines()
P = []
pattern = []
for line in lines:
    if line == '\n':
        P.append(pattern)
        pattern = []
    else:
        pattern.append(line.strip())
if len(pattern) > 0:
    P.append(pattern)

def find_horizontal(p):
    m = len(p)
    for i in range(m-1):
        if p[i] == p[i+1]:
            u = i-1
            v = i+2
            while u >= 0 and v < m and p[u] == p[v]:
                u -= 1
                v += 1
            if u < 0 or v >= m:
                return i+1
    return None

res = 0
for p in P:
    cnt = find_horizontal(p)
    if cnt == None:
        fp = list(map(''.join, zip(*p)))
        cnt = find_horizontal(fp)
    else:
        cnt = cnt*100
    res += cnt
print(res)