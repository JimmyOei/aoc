import numpy as np

input = open('./input_08.txt', 'r')
lines = input.readlines()
lines = [list(line.strip()) for line in lines]

n = len(lines)
m = len(lines[0])

ans = 0

ants = {}
for i in range(n):
  for j in range(m):
    if lines[i][j] != '.':
      if lines[i][j] not in ants:
        ants[lines[i][j]] = [(i, j)]
      else:
        ants[lines[i][j]].append((i, j))

for k in ants.values():
  for l in range(len(k)):
    for o in range(l + 1, len(k)):
      x1, y1 = k[o]
      x2, y2 = k[l]
      difx, dify = x2 - x1, y2 - y1
      newx1, newy1 = x1-difx, y1-dify
      newx2, newy2 = x2+difx, y2+dify
      if newx1 >= 0 and newx1 < n and newy1 >= 0 and newy1 < m and lines[newx1][newy1] != '#':
        lines[newx1][newy1] = '#'
        ans += 1
      if newx2 >= 0 and newx2 < n and newy2 >= 0 and newy2 < m and lines[newx2][newy2] != '#':
        lines[newx2][newy2] = '#'
        ans += 1
print(ans)