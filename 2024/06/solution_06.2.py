input = open('./input_06.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

copylines = lines.copy()

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

def isInLoop(maze, i, j, dir):
  curr = (i, j)
  while True:
    i, j = curr
    nexti, nextj = (i + dir[0], j + dir[1])
    if nexti < 0 or nexti >= n or nextj < 0 or nextj >= m:
      return False
    if maze[nexti][nextj] == '#':
      dir = turn_right(dir)
      continue
    if dir == (-1, 0):
      if maze[i][j] == 'v':
        return True
      maze[i] = maze[i][:j] + 'v' + maze[i][j + 1:]
    if dir == (0, 1):
      if maze[i][j] == '<':
        return True
      maze[i] = maze[i][:j] + '<' + maze[i][j + 1:]
    if dir == (1, 0):
      if maze[i][j] == '^':
        return True
      maze[i] = maze[i][:j] + '^' + maze[i][j + 1:]
    if dir == (0, -1):
      if maze[i][j] == '>':
        return True
      maze[i] = maze[i][:j] + '>' + maze[i][j + 1:]
    curr = (nexti, nextj)

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
  if dir == (-1, 0):
    lines[i] = lines[i][:j] + 'v' + lines[i][j + 1:]
  if dir == (0, 1):
    lines[i] = lines[i][:j] + '<' + lines[i][j + 1:]
  if dir == (1, 0):
    lines[i] = lines[i][:j] + '^' + lines[i][j + 1:]
  if dir == (0, -1):
    lines[i] = lines[i][:j] + '>' + lines[i][j + 1:]
  if not copylines[nexti][nextj] == '#':
    maze = lines.copy()
    maze[nexti] = maze[nexti][:nextj] + '#' + maze[nexti][nextj + 1:]
    copylines[nexti] = copylines[nexti][:nextj] + '#' + copylines[nexti][nextj + 1:]
    if isInLoop(maze, i, j, dir):
      cnt += 1
  curr = (nexti, nextj)
print(cnt)