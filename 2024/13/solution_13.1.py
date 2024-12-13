input = open('./input_13.txt', 'r')
lines = input.readlines()
lines = [line.strip().split(' ') for line in lines]

m = [[]]
for line in lines:
  if line == ['']:
    m.append([])
    continue
  if len(line) == 3:
    m[-1].append((int(line[1][2:-1]), int(line[2][2:])))
  else:
    m[-1].append(([int(line[2][2:-1]), int(line[3][2:])]))

def find_closest(x, y, px, py):
  closest = min(px // x, py // y)
  return closest, px - x * closest, py - y * closest

ans = 0
for l in m:
  ax, ay = l[0]
  bx, by = l[1]
  px, py = l[2]
  
  cb, cbx, cby = find_closest(bx, by, px, py)
  ca, cax, cay = find_closest(ax, ay, cbx, cby)
  if cax == 0 and cay == 0:
    lowestcost = ca * 3 + cb

  i = cb
  lowestcost = float("inf")
  prevx, prevy = cax, cay
  while i > 0:
    cy = py - i * by
    cx = px - i * bx
    ma, max, may = find_closest(ax, ay, cx, cy)
    if max == 0 and may == 0:
      cost = i + ma * 3
      if cost < lowestcost:
        lowestcost = cost
    i -= 1
  if lowestcost != float("inf"):
    ans += lowestcost

print(ans)