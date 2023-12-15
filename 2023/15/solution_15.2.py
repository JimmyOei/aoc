input = open('./input_15.txt', 'r')
lines = input.readlines()
L = lines[0].strip().split(',')

B = {}

for s in L:
    box = 0
    i = 0
    n = len(s)
    while i < n and not (s[i] == '=' or s[i] == '-'):
        box += ord(s[i])
        box *= 17
        box %= 256
        i += 1
    label = s[:i]
    op = s[i]
    if op == '-':
        if box in B:
            if label in B[box]:
                del B[box][label]

    else:
        i += 1
        value = int(s[i:])
        if box in B:
            B[box][label] = value
        else:
            B[box] = {label: value}

res = 0
for b, slots in B.items():
    bv = int(b)+1
    i = 1
    for s in slots.values():
        res += (bv * i * s)
        i += 1
print(res)