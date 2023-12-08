import math

input = open('./input_08.txt', 'r')
lines = input.readlines()

instr = lines[0].strip()
mp = {}
for line in lines[2:]:
    nodes = line.strip().split()
    mp[nodes[0]] = [nodes[2][1:-1], nodes[3][:-1]]

curr = [node for node in mp.keys() if node[-1] == 'A']
zs = []
n = len(instr)
step = 0
while len(curr) > 0:
    i = 0
    while len(curr) > 0 and i < n:
        newcurr = []
        ins = 0 if instr[i] == 'L' else 1
        while len(curr) > 0:
            c = curr.pop()
            newc = mp[c][ins]
            if newc[-1] == 'Z':
                zs.append((newc, i))
            else:
                newcurr.append(newc)
        curr = newcurr
        i += 1
        step += 1

cycles = []
for z, i in zs:
    step = 0
    i += 1
    if not i < n:
        i = 0
    c = mp[z][0 if instr[i] == 'L' else 1]
    step += 1
    i += 1
    while c != z:
        while c != z and i < n:
            c = mp[c][0 if instr[i] == 'L' else 1]
            i += 1
            step += 1
        i = 0
    cycles.append(step)
print(cycles)

res = math.lcm(*(cycles))
print(res)