import heapq

input = open('./input_17.txt', 'r')
lines = input.readlines()
M = [[int(i) for i in line.strip()] for line in lines]

m = len(M)
n = len(M[0])

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)
DIRS = [LEFT, RIGHT, UP, DOWN]

def opposite_dir(dir):
    if dir == LEFT: return RIGHT
    if dir == RIGHT: return LEFT
    if dir == UP: return DOWN
    return UP

END = (m-1, n-1)
MAX_CNT = 3

def within_M(i, j):
    return i < m and j < n and i >= 0 and j >= 0

# cost, straight count, position (x,y), direction
curr = [(0, 1, (0, 1), RIGHT), (0, 1, (1, 0), DOWN)]

vis = set()

res = 0
while len(curr) > 0:
    c = heapq.heappop(curr)
    cost, cnt, pos, dir = c
    
    if (pos, cnt, dir) in vis:
        continue
    vis.add((pos, cnt, dir))
    newcost = cost + M[pos[0]][pos[1]]
    if pos == END:
        res = newcost
        break
    
    opp_dir = opposite_dir(dir)
    for d in DIRS:
        if opp_dir == d:
            continue

        x = pos[0]+d[0]
        y = pos[1]+d[1]
        newcnt = cnt+1 if dir == d else 1
        if newcnt <= MAX_CNT and within_M(x, y):
            heapq.heappush(curr, (newcost, newcnt, (x, y), d))
print(res)