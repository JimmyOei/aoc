input = open('./input_21.txt', 'r')
lines = input.readlines()

L = [list(line.strip()) for line in lines]

m = len(L)
n = len(L[0])

def find_start():
  for i in range(m):
    for j in range(n):
      if L[i][j] == 'S':
        return (i, j)

start = find_start()

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
DIRS = [NORTH, EAST, SOUTH, WEST]

def within_L(i, j):
  return i >= 0 and j >= 0 and i < m and j < n

STEPS = 64

curr = [start]
for i in range(STEPS):
  newcurr = []
  while len(curr) > 0:
    x, y = curr.pop()
    for u, v in DIRS:
      nx = x+u
      ny = y+v
      if within_L(nx, ny) and L[nx][ny] != '#' and L[nx][ny] != i:
        newcurr.append((nx,ny))
        L[nx][ny] = i
  curr = newcurr

res = len(curr)
print(res)


