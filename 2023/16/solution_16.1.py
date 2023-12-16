input = open('./input_16.txt', 'r')
lines = input.readlines()
L = [list(line.strip()) for line in lines]

m = len(L)
n = len(L[0])

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

def dir_no(dir):
    if dir == LEFT: return 0
    if dir == RIGHT: return 1
    if dir == UP: return 2
    return 3


def within_L(i, j):
    return i < m and j < n and i >= 0 and j >= 0

def next_lights(i, j, dir):
    c = L[i][j]
    if c == '|' and (dir == RIGHT or dir == LEFT):
        return [(i, j, UP), (i, j, DOWN)]
    elif c == '-' and (dir == UP or dir == DOWN):
        return [(i, j, RIGHT), (i, j, LEFT)]
    elif c == '/':
        if dir == RIGHT:
            return [(i, j, UP)]
        elif dir == LEFT:
            return [(i, j, DOWN)]
        elif dir == UP:
            return [(i, j, RIGHT)]
        else:
            return [(i, j, LEFT)]
    elif c == '\\':
        if dir == RIGHT:
            return [(i, j, DOWN)]
        elif dir == LEFT:
            return [(i, j, UP)]
        elif dir == UP:
            return [(i, j, LEFT)]
        else:
            return [(i, j, RIGHT)]
    return [(i, j, dir)]

V = [[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]

res = 0
lights = [(0, -1, RIGHT)]
while len(lights) > 0:
    newlights = []
    while len(lights) > 0:
        l1, l2, dir = lights.pop()
        m1 = l1+dir[0]
        m2 = l2+dir[1]
        dirno = dir_no(dir)
        if within_L(m1, m2) and not V[m1][m2][dirno]:
            if sum(V[m1][m2]) == 0:
                res += 1
            newlights.extend(next_lights(m1, m2, dir))
            V[m1][m2][dirno] = True
    lights = newlights
print(res)