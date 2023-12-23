input = open('./input_23.txt', 'r')
lines = input.readlines()
M = [list(line.strip()) for line in lines]

m = len(M)
n = len(M[0])

def within_M(i, j):
    return i < m and j < n and i >= 0 and j >= 0

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)
DIRS = [UP, DOWN, RIGHT, LEFT]

start = (0, M[0].index('.'))
end = (m-1, M[m-1].index('.'))

nodes = [start, end]
for i in range(m):
  for j in range(n):
    if (i, j) != start and (i, j) != end and M[i][j] != '#':
      neighbours = 0
      for u, v in DIRS:
        ni = i+u
        nj = j+v
        if M[ni][nj] != '#':
          neighbours += 1
      if neighbours > 2:
        nodes.append((i, j))

adj = {node: {} for node in nodes}
for node in nodes:
  curr = [(node, None, set())]
  steps = 1
  while len(curr) > 0:
    newcurr = []
    while len(curr) > 0:
      cn, slopedir, vis = curr.pop()
      i, j = cn
      vis.add(cn)
      for u, v in DIRS:
        ni = i+u
        nj = j+v
        other = (ni, nj)

        if not within_M(ni, nj) or other in vis:
          continue

        if other in nodes:
          adj[node][other] = steps
          continue

        c = M[ni][nj]
        if c != '#':
          newcurr.append((other, None, vis.copy()))
    curr = newcurr
    steps += 1

vis = set()
def dfs(node):
  if node == end:
    return 0
  if node in vis:
    return -float("inf")
  
  cost = -float("inf")
  vis.add(node)
  for other, c in adj[node].items():
    cost = max(cost, dfs(other) + c)
  vis.remove(node)

  return cost
res = dfs(start)
print(res)
