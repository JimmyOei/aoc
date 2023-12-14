input = open('./input_14.txt', 'r')
lines = input.readlines()
L = [line.strip() for line in lines]
m = len(L)
n = len(L[0])

top_load = [m] * n
res = 0
for i, l in enumerate(L):
    for j, v in enumerate(l):
        if v == 'O':
            res += top_load[j]
            top_load[j] -= 1
        elif v == '#':
            top_load[j] = m-(i+1)
print(res)
