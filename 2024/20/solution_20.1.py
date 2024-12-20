import heapq 

input = open('./input_20.txt', 'r')
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
            start = (i, j, [(i, j)])
            break

stack = [start]
nocheatcost = 0
nocheatpath = []

cost = 0
while stack:
    length = len(stack)
    for _ in range(length):
      i, j, v = stack.pop()

      if lines[i][j] == 'E':
          nocheatcost = cost
          nocheatpath = v
          break
        
      for dir in [UP, DOWN, LEFT, RIGHT]:
          if i+dir[0] >= 0 and i+dir[0] < n and j+dir[1] >= 0 and j+dir[1] < m and (i+dir[0], j+dir[1]) not in v and lines[i+dir[0]][j+dir[1]] != '#':
              stack.append((i+dir[0], j+dir[1], v + [(i+dir[0], j+dir[1])]))
    cost += 1
    
k = 1            
for i, j in nocheatpath:
    lines[i][j] = str(k)
    k += 1

print(nocheatcost)
    
ans = 0
for i, j in nocheatpath:
    cost = int(lines[i][j])
    if i+2 < n and lines[i+1][j] == '#' and lines[i+2][j] != '.' and lines[i+2][j] != '#':
        if int(lines[i+2][j]) >= cost + 2 + 100:
            ans += 1
    if i-2 >= 0 and lines[i-1][j] == '#' and lines[i-2][j] != '.' and lines[i-2][j] != '#':
        if int(lines[i-2][j]) >= cost + 2 + 100:
            ans += 1
    if j+2 < m and lines[i][j+1] == '#' and lines[i][j+2] != '.' and lines[i][j+2] != '#':
        if int(lines[i][j+2]) >= cost + 2 + 100:
            ans += 1
    if j-2 >= 0 and lines[i][j-1] == '#' and lines[i][j-2] != '.' and lines[i][j-2] != '#':
        if int(lines[i][j-2]) >= cost + 2 + 100:
            ans += 1
print(ans)