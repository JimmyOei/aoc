input = open('./input_12.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]


ans = 0
for l in range(len(lines)):
  for m in range(len(lines[l])):
    if lines[l][m].isupper():
      k = lines[l][m]
      per = 0
      cnt = 0
      s = [(l, m)]
      vis = ()
      vis += ((l, m),)
      while len(s) > 0:
        i, j = s.pop()
        cnt += 1
        per += 4
        lines[i] = lines[i][:j] + k.lower() + lines[i][j+1:]
        if j > 0 and (lines[i][j-1] == k or lines[i][j-1] == k.lower()):
          if (i, j-1) not in vis:
            s.append((i, j-1))
            vis += ((i, j-1),)
          per -= 1
        if j < len(lines[i])-1 and (lines[i][j+1] == k or lines[i][j+1] == k.lower()):
          if (i, j+1) not in vis:
            s.append((i, j+1))
            vis += ((i, j+1),)
          per -= 1
        if i > 0 and (lines[i-1][j] == k or lines[i-1][j] == k.lower()):
          if (i-1, j) not in vis:
            s.append((i-1, j))
            vis += ((i-1, j),)
          per -= 1
        if i < len(lines)-1 and (lines[i+1][j] == k or lines[i+1][j] == k.lower()):
          if (i+1, j) not in vis:
            s.append((i+1, j))
            vis += ((i+1, j),)
          per -= 1
      ans += per*cnt
print(ans)
    