input = open('./input_12.txt', 'r')
lines = input.readlines()
lines = [list(line.strip()) for line in lines]

dup = {}
cnts = {}

ans = 0
vis = ()
for l in range(len(lines)):
  for m in range(len(lines[l])):
    if (l, m) in vis:
      continue
    k = lines[l][m]
    if k in dup:
      dup[k] += 1
    else:
      dup[k] = 1
    newk = k+str(dup[k])
    cnts[newk] = 0
    s = [(l, m)]
    while len(s) > 0:
      i, j = s.pop()
      if i >= 0 and i < len(lines) and j >= 0 and j < len(lines[i]) and lines[i][j] == k:
        lines[i][j] = newk
        vis += ((i, j),)
        cnts[newk] += 1
        s.append((i-1, j))
        s.append((i+1, j))
        s.append((i, j-1))
        s.append((i, j+1))

def cntneighbours(i, j, k, isk=False):
  if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
    return 0
  cnt = 0
  x = 0
  y = 0
  left = False
  right = False
  up = False
  down = False
  if i+1 < len(lines) and lines[i+1][j] == k:
    cnt += 1
    y += 1
    down = True
  if i-1 >= 0 and lines[i-1][j] == k:
    cnt += 1
    y += 1
    up = True
  if j+1 < len(lines[i]) and lines[i][j+1] == k:
    cnt += 1
    x += 1
    right = True
  if j-1 >= 0 and lines[i][j-1] == k:
    cnt += 1
    x += 1
    left = True
  if not isk:
    cntisk = 0
    if up and left:
      if j-1 >= 0 and i-1 >= 0 and lines[i-1][j-1] == k:
        cntisk += 1
    if up and right:
      if j+1 < len(lines[i]) and i-1 >= 0 and lines[i-1][j+1] == k:
        cntisk += 1
    if down and left:
      if j-1 >= 0 and i+1 < len(lines) and lines[i+1][j-1] == k:
        cntisk += 1
    if down and right:
      if j+1 < len(lines[i]) and i+1 < len(lines) and lines[i+1][j+1] == k:
        cntisk += 1
    return cntisk
  if cnt == 2:
    if x == 2 or y == 2:
      return 0
    return 2
  return cnt

for k, v in cnts.items():
  corners = 0
  for l in range(len(lines)):
    for m in range(len(lines[l])):
      if lines[l][m] == k:
        cnt = cntneighbours(l, m, k, True)
        if cnt == 1:
          corners += 2
        if cnt == 2:
          corners += 1
      else:
        corners += cntneighbours(l, m, k, False)
  if v == 1:
    ans += 4
  ans += (corners)*v
print(ans)
    