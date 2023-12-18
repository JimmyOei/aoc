input = open('./input_18.txt', 'r')
lines = input.readlines()
L = [(int(l[2][2:7], 16), int(l[2][7])) for l in [line.split() for line in lines]]

row_cross = {0: []}
x = 0
y = 0
area = 0
sum_steps = 0
for steps, dir in L:
    sum_steps += steps
    newx = x
    newy = y
    if dir == 0:
        newx += steps
    elif dir == 2:
        newx -= steps
    elif dir == 1:
        newy += steps
    elif dir == 3:
        newy -= steps

    area += (x*newy) - (y*newx)
    x = newx
    y = newy
area = abs(area) / 2
print(int(area + sum_steps / 2 + 1))
