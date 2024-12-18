input = open('./input_18.txt', 'r')
lines = input.readlines()
lines = [list(int(num) for num in line.strip().split(',')) for line in lines]

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

n = 71

start = (0, 0)
end = (70, 70)

mp = [['.' for _ in range(n)] for _ in range(n)]

def bfs():
  s = [start]
  steps = 0
  visited = set()
  visited.add(start)
  while s:
      l = len(s)
      for _ in range(l):
          x, y = s.pop(0)
          if (x, y) == end:
              return steps
          for dx, dy in [UP, DOWN, LEFT, RIGHT]:
              nx, ny = x + dx, y + dy
              if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and mp[ny][nx] == '.':
                  visited.add((nx, ny))
                  s.append((nx, ny))
      steps += 1
  return -1

for x, y in lines:
    mp[y][x] = '#'
    if bfs() == -1:
        print(x, y)
        break