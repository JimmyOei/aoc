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
    l = list(line)
    newl = []
    for c in l:
        if c == '#':
            newl += ['#', '#']
        if c == '.':
            newl += ['.', '.']
        if c == 'O':
            newl += ['[', ']']
        if c == '@':
            newl += ['@', '.']
    mp.append(newl)

for line in mvslines:
    for c in line:
        mvs.append(get_move(c))

def push_multiple(x, y, dx, dy):
    pos = [[(x, y)]]
    iter = 0
    if mp[x][y] == '[':
        pos[0].append((x, y+1))
    if mp[x][y] == ']':
        pos[0].append((x, y-1))

    while pos[iter] != []:
        n = len(pos[iter])
        pos.append([])
        for i in range(n):
            px, py = pos[iter][i]
            npx, npy = px + dx, py + dy
            if npx < 0 or npx >= len(mp) or npy < 0 or npy >= len(mp[npx]):
                continue
            if mp[npx][npy] == '[':
                if (npx, npy) not in pos[iter+1]:
                  pos[iter+1].append((npx, npy))
                  pos[iter+1].append((npx, npy+1))
            if mp[npx][npy] == ']':
                if (npx, npy) not in pos[iter+1]:
                  pos[iter+1].append((npx, npy))
                  pos[iter+1].append((npx, npy-1))
        iter += 1
    
    del pos[-1]

    possible = True
    for i in range(iter):
      for posx, posy in pos[i]:
          dposx, dposy = posx + dx, posy + dy
          if dposx < 0 or dposx >= len(mp) or dposy < 0 or dposy >= len(mp[dposx]):
              possible = False
              break
          if mp[dposx][dposy] == '#':
              possible = False
              break
    
    if possible:
        for i in reversed(range(iter)):
          for posx, posy in pos[i]:
              dposx, dposy = posx + dx, posy + dy
              mp[dposx][dposy] = mp[posx][posy]
              mp[posx][posy] = '.'
        return (x + dx, y + dy)
    return (x, y)


def move(c, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= len(mp) or ny < 0 or ny >= len(mp[nx]):
        return (x, y)
    if mp[nx][ny] == '#':
        return (x, y)
    elif mp[nx][ny] == '[' or mp[nx][ny] == ']':
        nnx, nny = (-1, -1)
        if dx == 0:
            nnx, nny = move(mp[nx][ny], nx, ny, dx, dy)
        else:
          nnx, nny = push_multiple(nx, ny, dx, dy)
        if nnx == nx and nny == ny:
            return (x, y)
    if mp[nx][ny] == '.':
        mp[nx][ny] = c
        mp[x][y] = '.'
        return (nx, ny)
    return (x, y)

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
      if mp[i][j] == '[':
        ans += i*100 + j
print(ans)