import heapq

input = open('./input_16.txt', 'r')
lines = input.readlines()
lines = [list(line.strip()) for line in lines]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


n = len(lines)
m = len(lines[0])

start = (0, 0, 0, [])
for i in range(n):
    for j in range(m):
        if lines[i][j] == 'S':
            start = (0, i, j, RIGHT, [(i, j)])
            break

def find(visited):
  stack = [start]
  visited.add((start[1], start[2]))
  while stack:
      p, i, j, dir, path = heapq.heappop(stack)
          
      if lines[i][j] == 'E':
          return path, p

      if i+1 < n and (i+1, j) not in visited and lines[i+1][j] != '#':
          if dir == DOWN:
              heapq.heappush(stack, (p+1, i+1, j, DOWN, path + [(i+1, j)]))
              visited.add((i+1, j))
          elif dir == LEFT or dir == RIGHT:
              heapq.heappush(stack, (p+1001, i+1, j, DOWN, path + [(i+1, j)]))
              visited.add((i+1, j))
      if i-1 >= 0 and (i-1, j) not in visited and lines[i-1][j] != '#':
          if dir == UP:
              heapq.heappush(stack, (p+1, i-1, j, UP, path + [(i-1, j)]))
              visited.add((i-1, j))
          elif dir == LEFT or dir == RIGHT:
              heapq.heappush(stack, (p+1001, i-1, j, UP, path + [(i-1, j)]))
              visited.add((i-1, j))
      if j+1 < m and (i, j+1) not in visited and lines[i][j+1] != '#':
          if dir == RIGHT:
              heapq.heappush(stack, (p+1, i, j+1, RIGHT, path + [(i, j+1)]))
              visited.add((i, j+1))
          elif dir == UP or dir == DOWN:
              heapq.heappush(stack, (p+1001, i, j+1, RIGHT, path + [(i, j+1)]))
              visited.add((i, j+1))
      if j-1 >= 0 and (i, j-1) not in visited and lines[i][j-1] != '#':
          if dir == LEFT:
              heapq.heappush(stack, (p+1, i, j-1, LEFT, path + [(i, j-1)]))
              visited.add((i, j-1))
          elif dir == UP or dir == DOWN:
              heapq.heappush(stack, (p+1001, i, j-1, LEFT, path + [(i, j-1)]))
              visited.add((i, j-1))
  return [], float('inf')

path, cost = find(set())

anspath = path
for x, y in path:
  newset = set()
  newset.add((x, y))
  newpath, newcost = find(newset)
  if newcost == cost:
    for xx, yy in newpath:
        if (xx, yy) not in anspath:
            anspath.append((xx, yy))

print(len(anspath))