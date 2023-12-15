input = open('./input_15.txt', 'r')
lines = input.readlines()
L = lines[0].strip().split(',')

res = 0
for s in L:
    curr = 0
    for i in s:
        curr += ord(i)
        curr *= 17
        curr %= 256
    res += curr
print(res)
