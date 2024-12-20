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
      i, j, v = stack.pop(0)

      if lines[i][j] == 'E':
          nocheatcost = cost
          nocheatpath = v
          break
        
      for dir in [UP, DOWN, LEFT, RIGHT]:
          if i+dir[0] >= 0 and i+dir[0] < n and j+dir[1] >= 0 and j+dir[1] < m and (i+dir[0], j+dir[1]) not in v and lines[i+dir[0]][j+dir[1]] != '#':
              stack.append((i+dir[0], j+dir[1], v + [(i+dir[0], j+dir[1])]))
    cost += 1
    
k = 0          
for i, j in nocheatpath:
    lines[i][j] = str(k)
    k += 1

cheatssavinglimit = 100
cheatcost = 20
ans = 0

def calc_cheat(cost, i, j):
    stack = [(i, j)]
    cheat = 0
    visited = set()
    cnt = 0
    while stack and cheat <= cheatcost:
        length = len(stack)
        for _ in range(length):
          i, j = stack.pop(0)
          if (i, j) in visited:
              continue
          visited.add((i, j))

          if lines[i][j] != '.' and lines[i][j] != '#':
              if int(lines[i][j]) >= cost + cheat + cheatssavinglimit:
                  cnt += 1
            
          for dir in [UP, DOWN, LEFT, RIGHT]:
              if i+dir[0] >= 0 and i+dir[0] < n and j+dir[1] >= 0 and j+dir[1] < m:
                  stack.append((i+dir[0], j+dir[1]))
        cheat += 1
    return cnt

for i, j in nocheatpath:
    cost = int(lines[i][j])
    ans += calc_cheat(cost, i, j)
      
print(ans)