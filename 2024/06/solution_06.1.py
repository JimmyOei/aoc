input = open('./input_06.txt', 'r')
lines = input.readlines()

n = len(lines)
m = len(lines[0])

def turn_right(dir):
  if dir == (-1, 0):
    return (0, 1)
  if dir == (0, 1):
    return (1, 0)
  if dir == (1, 0):
    return (0, -1)
  if dir == (0, -1):
    return (-1, 0)

def find_start():
  for i in range(n):
    for j in range(m):
      if lines[i][j] == '^':
        pos = (i, j)
        dir = (-1, 0)
        return pos, dir
      if lines[i][j] == 'v':
        pos = (i, j)
        dir = (1, 0)
        return pos, dir
      if lines[i][j] == '<':
        pos = (i, j)
        dir = (0, -1)
        return pos, dir
      if lines[i][j] == '>':
        pos = (i, j)
        dir = (0, 1)
        return pos, dir

startpos, dir = find_start()

cnt = 0
curr = startpos
while True:
  i, j = curr
  nexti, nextj = (i + dir[0], j + dir[1])
  if nexti < 0 or nexti >= n or nextj < 0 or nextj >= m:
    break
  if lines[nexti][nextj] == '#':
    dir = turn_right(dir)
    continue
  if lines[i][j] != 'X':
    cnt += 1
    lines[i] = lines[i][:j] + 'X' + lines[i][j + 1:]
  curr = (nexti, nextj)
print(cnt+1)