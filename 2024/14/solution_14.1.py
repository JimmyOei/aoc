input = open('./input_14.txt', 'r')
lines = input.readlines()
lines = [line.strip().split(' ') for line in lines]

robots = []
for line in lines:
  point = line[0].split(',')
  vel = line[1].split(',')
  robots.append([[int(point[0][2:]), int(point[1])], [int(vel[0][2:]), int(vel[1])]])

print(robots)

m = 101
n = 103
# for r in robots:
#   m = max(m, r[0][0]+1)
#   n = max(n, r[0][1]+1)

print(m, n)

def calc_next_point(px, py, vx, vy):
  nextx = px+vx
  nexty = py+vy
  if nextx < 0:
    nextx = m + nextx
  if nextx >= m:
    nextx = nextx - m
  if nexty < 0:
    nexty = n + nexty
  if nexty >= n:
    nexty = nexty - n

  return [nextx, nexty]

seconds = 100

for s in range(seconds):
  for r in robots:
    px, py = r[0]
    vx, vy = r[1]
    r[0] = calc_next_point(px, py, vx, vy)

hm1 = m // 2
hm2 = hm1 - 1 if 2*hm1 == m else hm1
hn1 = n // 2
hn2 = hn1 - 1 if 2*hn1 == n else hn1
print(hm1, hm2, hn1, hn2)
# q1 = [(0, 0), (hm, 0)]
# q2 = [(hm, 0), (hm, hn)]
# q3 = [(0, hn), (hm, n)]
# q4 = [(hm, hn), (m, n)]

q1sum = 0
q2sum = 0
q3sum = 0
q4sum = 0
for r in robots:
  px, py = r[0]
  if px < hm1 and py < hn1:
    q1sum += 1
  elif px > hm2 and py < hn1:
    q2sum += 1
  elif px < hm1 and py > hn2:
    q3sum += 1
  elif px > hm1 and py > hn2:
    q4sum += 1
print(q1sum, q2sum, q3sum, q4sum)
ans = q1sum * q2sum * q3sum * q4sum
print(ans)

