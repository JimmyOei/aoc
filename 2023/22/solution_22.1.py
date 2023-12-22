input = open('input_22.txt', 'r')
lines = input.readlines()

L = [(tuple(int(i) for i in l[0].split(',')), tuple(int(i) for i in l[1].split(','))) for l in [line.strip().split('~') for line in lines]]
B = sorted(L, key=lambda x: min(x[0][2], x[1][2]))

m = 0
n = 0
for b in B:
  m = max(m, max(b[0][0], b[0][0]))
  n = max(n, max(b[0][1], b[1][1]))
m += 1
n += 1

plain = [[None for _ in range(n)] for _ in range(m)]
supporting = [[] for _ in range(len(B))]
supports = [0 for _ in range(len(B))]

for i, b in enumerate(B):
  x, y, z = b[0]
  u, v, w = b[1]
  minx = min(x, u)
  maxx = max(x, u)
  miny = min(y, v)
  maxy = max(y, v)
  in_area = []
  currx = minx
  while currx <= maxx:
    curry = miny
    while curry <= maxy:
      if plain[currx][curry] != None:
        in_area.append(plain[currx][curry])
      curry += 1
    currx += 1
  
  in_area = list(set(in_area))
  in_area.sort(key = lambda x: x[1], reverse=True)
  at_z = in_area[0][1] if len(in_area) > 0 else 0
  for k in in_area:
    if k[1] == at_z:
      supporting[k[0]].append(i)
      supports[i] += 1
    else:
      break

  at_z += 1 + abs(z - w)
  currx = minx
  curry = miny
  while currx <= maxx:
    curry = miny
    while curry <= maxy:
      plain[currx][curry] = (i, at_z)
      curry += 1
    currx += 1
  
res = 0
for i in supporting:
  disintegrate = True
  for j in i:
    if supports[j] == 1:
      disintegrate = False
      break
  if disintegrate:
    res += 1

print(res)