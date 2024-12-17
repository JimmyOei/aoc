input = open('./input_17.txt', 'r')
lines = input.readlines()
lines = [line.strip().split(' ') for line in lines]

rA = int(lines[0][2])
rB = int(lines[1][2])
rC = int(lines[2][2])
program = [int(num) for num in lines[4][1].split(',')]
n = len(program)

# 0: A // 2^i -> A
# 1: B XOR i -> B
# 2: i % 8 -> B
# 3: A == 0 -> nothing, else ipointer to i
# 4: B XOR C -> B, reads i but ignores it
# 5: i % 8 -> output
# 6: A // 2^i -> B
# 7: A // 2^i -> C

output = []
i = 0
while i+1 < n:
    op = program[i]
    cop = program[i+1]
    if cop == 4:
        cop = rA
    elif cop == 5:
        cop = rB
    elif cop == 6:
        cop = rC
    if op == 0:
        rA = rA // (2**cop)
        i += 2
    elif op == 1:
        rB = rB ^ cop
        i += 2
    elif op == 2:
        rB = cop % 8
        i += 2
    elif op == 3:
        if rA == 0:
            i += 1
        else:
            i = cop
    elif op == 4:
        rB = rB ^ rC
        i += 2
    elif op == 5:
        output.append(cop % 8)
        i += 2
    elif op == 6:
        rB = rA // (2**cop)
        i += 2
    elif op == 7:
        rC = rA // (2**cop)
        i += 2

print(','.join([str(num) for num in output]))
    