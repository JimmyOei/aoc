input = open('./input_18.txt', 'r')
lines = input.readlines()
L = [(l[0], int(l[1]), l[2][1:-1]) for l in [line.split() for line in lines]]

row_cross = {0: []}
x = 0
y = 0
area = 0
sum_steps = 0
for dir, steps, col in L:
    sum_steps += steps
    newx = x
    newy = y
    if dir == 'R':
        newx += steps
    elif dir == 'L':
        newx -= steps
    elif dir == 'U':
        newy += steps
    elif dir == 'D':
        newy -= steps

    area += (x*newy) - (y*newx)
    x = newx
    y = newy
area = abs(area) / 2
print(int(area + sum_steps / 2 + 1))
