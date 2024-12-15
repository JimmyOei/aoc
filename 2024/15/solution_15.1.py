input = open('./input_15.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
mplines = []
mvslines = []
for line in lines:
    if line == '':
        continue
    if line[0] == '#':
        mplines.append(line)
    else:
        mvslines.append(line)

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

def get_move(c):
    if c == '<':
        return LEFT
    if c == '>':
        return RIGHT
    if c == '^':
        return UP
    if c == 'v':
        return DOWN

mp = []
mvs = []

for line in mplines:
    mp.append(list(line))

for line in mvslines:
    for c in line:
        mvs.append(get_move(c))

def move(c, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= len(mp) or ny < 0 or ny >= len(mp[nx]):
        return (x, y)
    if mp[nx][ny] == '#':
        return (x, y)
    if mp[nx][ny] == 'O':
        nnx, nny = move('O', nx, ny, dx, dy)
        if nnx == nx and nny == ny:
            return (x, y)
    if mp[nx][ny] == '.':
        mp[nx][ny] = c
        mp[x][y] = '.'
        return (nx, ny)

def find_start_robot():
  for i in range(len(mp)):
      for j in range(len(mp[i])):
          if mp[i][j] == '@':
              return (i, j)

robot = find_start_robot()

for m in mvs:
    i, j = m
    robot = move('@', robot[0], robot[1], i, j)

ans = 0
for i in range(len(mp)):
    for j in range(len(mp[i])):
      if mp[i][j] == 'O':
        ans += i*100 + j
print(ans)