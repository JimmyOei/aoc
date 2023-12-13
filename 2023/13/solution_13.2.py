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

DIF_ALLOWED = 1

def dif(s1, s2):
    d = 0  
    for i in range(len(s1)):  
        if s1[i] != s2[i]:  
            d += 1
    return d

def find_horizontal(p):
    m = len(p)
    for i in range(m-1):
        u = i
        v = i+1
        sumdif = 0
        while u >= 0 and v < m and sumdif <= DIF_ALLOWED:
            sumdif += dif(p[u], p[v])
            u -= 1
            v += 1
        if sumdif == DIF_ALLOWED and (u < 0 or v >= m):
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