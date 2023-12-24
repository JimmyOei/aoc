input = open('input_24.txt', 'r')
lines = input.readlines()
L = [(tuple(int(i) for i in l[0].split(',')), 
      tuple(int(i) for i in l[1].split(','))) 
      for l in [line.strip().split('@') for line in lines]]

F = []

for p, v in L:
  px, py, pz = p
  vx, vy, vz = v
  m = vy / vx
  c = py - m*px
  F.append((m, c, px, py, vx))

n = len(F)

MIN = 200000000000000
MAX = 400000000000000

res = 0
for i in range(n):
  m, c, px, py, vx = F[i]
  for j in range(i+1, n):
    om, oc, opx, opy, ovx = F[j]
    try:
      isx = (oc - c) / (m - om)
      isy = m * isx + c
      if min(isx, isy) >= MIN and max(isx, isy) <= MAX \
        and ((vx > 0 and isx >= px) or (vx < 0 and isx <= px)) \
        and ((ovx > 0 and isx >= opx) or (ovx < 0 and isx <= opx)):
        res += 1
    except ZeroDivisionError:
      continue
print(res)