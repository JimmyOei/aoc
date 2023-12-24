import sympy

input = open('input_24.txt', 'r')
lines = input.readlines()
L = [(tuple(int(i) for i in l[0].split(',')), 
      tuple(int(i) for i in l[1].split(','))) 
      for l in [line.strip().split('@') for line in lines]]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols('xr, yr, zr, vxr, vyr, vzr')

equations = []

for p, v in L:
  px, py, pz = p
  vx, vy, vz = v
  equations.append((xr - px) * (vy - vyr) - (yr - py) * (vx - vxr))
  equations.append((yr - py) * (vz - vzr) - (zr - pz) * (vy - vyr))

answers = sympy.solve(equations)
res = answers[0][xr] + answers[0][yr] + answers[0][zr]

print(answers, res)