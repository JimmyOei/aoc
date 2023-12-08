input = open('./input_08.txt', 'r')
lines = input.readlines()

instr = lines[0].strip()
mp = {}
for line in lines[2:]:
    nodes = line.strip().split()
    mp[nodes[0]] = [nodes[2][1:-1], nodes[3][:-1]]

curr = "AAA"
n = len(instr)
res = 0
while curr != "ZZZ":
    i = 0
    while curr != "ZZZ" and i < n:
        if instr[i] == 'L':
            curr = mp[curr][0]
        else:
            curr = mp[curr][1]
        i += 1
        res += 1
print(res)