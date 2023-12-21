# credits to https://www.youtube.com/watch?v=9UOMZSL0JTg&ab_channel=HyperNeutrino

input = open('./input_21.txt', 'r')
lines = input.readlines()

L = [list(line.strip()) for line in lines]

m = len(L)

start = (m // 2, m // 2)

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
DIRS = [NORTH, EAST, SOUTH, WEST]

def within_L(i, j):
  return i >= 0 and j >= 0 and i < m and j < m

curr = [start]
def fill(start, steps):
  curr = [start]
  vis = set(curr)
  prevstate = 1
  prevprevstate = 0
  for _ in range(steps):
    newcurr = []
    while len(curr) > 0:
      y, x = curr.pop()
      for u, v in DIRS:
        ny = y+u
        nx = x+v
        if within_L(ny, nx) and L[ny][nx] != '#' and not (ny, nx) in vis:
          newcurr.append((ny,nx))
          vis.add((ny, nx))
    curr = newcurr
    currstate = prevprevstate + len(curr)
    prevprevstate = prevstate
    prevstate = currstate
  return prevstate

STEPS = 26501365

grid_width = STEPS // m - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(start, m * 2 + 1)
even_points = fill(start, m * 2)

corner_t = fill((m - 1, start[1]), m - 1)
corner_r = fill((start[0], 0), m - 1)
corner_b = fill((0, start[1]), m - 1)
corner_l = fill((start[0], m - 1), m - 1)

small_tr = fill((m - 1, 0), m // 2 - 1)
small_tl = fill((m - 1, m - 1), m // 2 - 1)
small_br = fill((0, 0), m // 2 - 1)
small_bl = fill((0, m - 1), m // 2 - 1)

large_tr = fill((m - 1, 0), m * 3 // 2 - 1)
large_tl = fill((m - 1, m - 1), m * 3 // 2 - 1)
large_br = fill((0, 0), m * 3 // 2 - 1)
large_bl = fill((0, m - 1), m * 3 // 2 - 1)

res = odd * odd_points + \
      even * even_points + \
      corner_t + corner_r + corner_b + corner_l + \
      (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) + \
      grid_width * (large_tr + large_tl + large_br + large_bl)

print(res)
