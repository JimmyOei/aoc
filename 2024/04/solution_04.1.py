input = open('./input_04.txt', 'r')
lines = input.readlines()
lines = [list(line.strip()) for line in lines]

n = len(lines)
m = len(lines[0])
ans = 0

for line in lines:
  strline = ''.join(line)
  ans += strline.count("XMAS") + strline.count("SAMX")

vertlines = list(map(list, zip(*lines)))
for line in vertlines:
  strline = ''.join(line)
  ans += strline.count("XMAS") + strline.count("SAMX")

rightdiagonallines = [[] for i in range(n*2)]
for i in range(n):
  for j in range(m):
    index = i-j
    if index < 0:
      index = -index + n - 1
    rightdiagonallines[index].append(lines[i][j])

for line in rightdiagonallines:
  strline = ''.join(line)
  ans += strline.count("XMAS") + strline.count("SAMX")

reversedlines = [line[::-1] for line in lines]
leftdiagonallines = [[] for i in range(n*2)]
for i in range(n):
  for j in range(m):
    index = i-j
    if index < 0:
      index = -index + len(reversedlines) - 1
    leftdiagonallines[index].append(reversedlines[i][j])

for line in leftdiagonallines:
  strline = ''.join(line)
  ans += strline.count("XMAS") + strline.count("SAMX")

print(ans)



