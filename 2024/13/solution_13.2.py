import sympy as sp

input = open('./input_13.txt', 'r')
lines = input.readlines()
lines = [line.strip().split(' ') for line in lines]

plus = 10000000000000
m = [[]]
for line in lines:
  if line == ['']:
    m.append([])
    continue
  if len(line) == 3:
    m[-1].append((int(line[1][2:-1]) + plus , int(line[2][2:]) + plus))
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

  A, B = sp.symbols('A B')
  eq1 = sp.Eq(A * ax + B * bx, px)
  eq2 = sp.Eq(A * ay + B * by, py)

  sol = sp.solve((eq1, eq2), (A, B))

  if sol[A] > 0 and sol[B] > 0 and sol[A].is_integer and sol[B].is_integer:
    ans += sol[A] * 3 + sol[B]


print(ans)