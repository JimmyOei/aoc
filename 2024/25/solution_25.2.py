input = open('./input_25.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
lines.append('') # for last schematic
  

locks = []
keys = []

n = len(lines[0])
m = 0
while lines[m] != '':
  m += 1

schematic = []
for line in lines:
    if line == '':
        if schematic[0] == ['#' for _ in range(len(schematic[0]))]:
          heights = [-1 for _ in range(len(schematic[0]))]
          for idx in reversed(range(len(schematic))):
            row = schematic[idx]
            for i in range(len(row)):
              if row[i] == '#' and heights[i] == -1:
                heights[i] = idx
          locks.append(heights)
        else:
          heights = [-1 for _ in range(len(schematic[0]))]
          for idx in range(len(schematic)):
            row = schematic[idx]
            for i in range(len(row)):
              if row[i] == '#' and heights[i] == -1:
                heights[i] = m-idx-1
          keys.append(heights)
        schematic = []
    else:
      schematic.append(list(line))

ans = 0
for lock in locks:
  for key in keys:
    correct = True
    for i in range(n):
      if lock[i] + key[i] > m-2:
        correct = False
        break
    if correct:
      ans += 1
print(ans)