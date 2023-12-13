input = open('./input_10.txt', 'r')
lines = input.readlines()
L = [list(line.strip()) for line in lines]
m = len(L)
n = len(L[0])

# options connected directions
north = ['|', '7', 'F']
south = ['|', 'L', 'J']
east = ['-', '7', 'J']
west = ['-', 'L', 'F']

def is_valid(i, j):
    if i < 0 or j < 0 or not i < m or not j < n:
        return False
    return True

def is_connected(A, option):
    i, j = A
    if not is_valid(i, j):
        return False

    if L[i][j] in option:
        return True
    return False

# directions
up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)


def move(A, direction):
    return tuple(map(sum, zip(A, direction)))

dirs_opts = [(up, north), (down, south), (left, west), (right, east)]

def get_dirs_opts(c):
    if c == '|':
        return [dirs_opts[0], dirs_opts[1]]
    if c == '-':
        return [dirs_opts[2], dirs_opts[3]]
    if c == 'L':
        return [dirs_opts[0], dirs_opts[3]] 
    if c == 'J':
        return [dirs_opts[0], dirs_opts[2]] 
    if c == '7':
        return [dirs_opts[1], dirs_opts[2]]
    if c == 'F':
        return [dirs_opts[1], dirs_opts[3]]
    return dirs_opts

S = None
for i, l in enumerate(L):
    if 'S' in l:
        S = (i, l.index('S'))

P = [[None]*n for _ in range(m)]

def opposite_opt(opt):
    if opt is north:
        return south
    if opt is south:
        return north
    if opt is west:
        return east
    return west

tmp = []
for dir, opt in dirs_opts:
    B = move(S, dir)
    if is_connected(B, opt):
        if len(tmp) > 0:
            tmp = set(tmp) & set(opposite_opt(opt))
            break
        else:
            tmp = opposite_opt(opt)

P[S[0]][S[1]] = list(tmp)[0]

curr = [(S, 'S')]
while len(curr) > 0:
    newcurr = []
    while len(curr) > 0:
        A, c = curr.pop()
        for dir, opt in get_dirs_opts(c):
            B = move(A, dir)
            if is_connected(B, opt):
                Bc = L[B[0]][B[1]]
                newcurr.append((B, Bc))
                P[B[0]][B[1]] = Bc
                L[B[0]][B[1]] = '.'
    curr = newcurr

inversion_corner = ['L', 'J']

res = 0
for i, row in enumerate(P):
    in_between = False
    j = 0
    while j < n:
        v = row[j]
        if v == '|' or v in inversion_corner:
            in_between = not in_between
        elif in_between and v == None:
            res += 1
        j += 1

print(res)

