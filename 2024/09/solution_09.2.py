input = open('./input_09.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
disk = [int(x) for x in list(lines[0])]

n = len(disk)

gaps = [0] * n
ids = [0] * n
cnts = [0] * n

idi = 0
for i in range(n):
  if i % 2 != 0:
    gaps[i] = disk[i]
  else:
    ids[i] = idi
    cnts[i] = disk[i]
    idi += 1

j = n - 1
while j > 0:
  if cnts[j] == 0:
    j -= 1
    continue
  i = 0
  jcnt = cnts[j]
  while i < n and i < j:
    if gaps[i] >= jcnt:
      if gaps[i] > jcnt:
        gaps.insert(i + 1, gaps[i] - jcnt)
        ids.insert(i + 1, 0)
        cnts.insert(i + 1, 0)
        j += 1
      gaps[i] = 0
      cnts[j] = 0
      ids[i] = ids[j]
      ids[j] = 0
      cnts[i] = jcnt
      gaps[j] = jcnt
      break
    i += 1
  j -= 1

ans = 0
k = 0
for i in range(n):
  if ids[i] == 0:
    k += gaps[i]
  for l in range(cnts[i]):
    ans += ids[i] * k
    k += 1

print(ans)
        