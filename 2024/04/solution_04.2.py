import re

input = open('./input_04.txt', 'r')
lines = input.readlines()
lines = [list(line.strip()) for line in lines]

n = len(lines)
m = len(lines[0])
mas = []
ans = 0

rightbotdiagonallines = [[] for i in range(n*2)]
rightbotcoords = [[] for i in range(n*2)]
for i in range(n):
  for j in range(m):
    index = i-j
    if index < 0:
      index = -index + n - 1
    rightbotdiagonallines[index].append(lines[i][j])
    rightbotcoords[index].append((i, j))

reversedlines = [line[::-1] for line in lines]
leftbotdiagonallines = [[] for i in range(n*2)]
leftbotcoords = [[] for i in range(n*2)]
for i in range(n):
  for j in range(m):
    index = i-j
    if index < 0:
      index = -index + len(reversedlines) - 1
    leftbotdiagonallines[index].append(reversedlines[i][j])
    leftbotcoords[index].append((i, m-j-1))


for idx, line in enumerate(rightbotdiagonallines):
  strline = ''.join(line)
  find = [m.start() for m in re.finditer('MAS', strline)] + [m.start() for m in re.finditer('SAM', strline)]
  for f in find:
    coords = rightbotcoords[idx][f+1]
    if coords in mas:
      mas.remove(coords)
      ans += 1
    else:
      mas.append(coords)

for idx, line in enumerate(leftbotdiagonallines):
  strline = ''.join(line)
  find = [m.start() for m in re.finditer('MAS', strline)] + [m.start() for m in re.finditer('SAM', strline)]
  for f in find:
    coords = leftbotcoords[idx][f+1]
    if coords in mas:
      mas.remove(coords)
      ans += 1
    else:
      mas.append(coords)

print(ans)



