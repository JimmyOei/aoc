import re

def mul(x, y):
    return x * y

input = open('./input_03.txt', 'r')
lines = input.readlines()

do = True

ans = 0
for line in lines:
  funcs = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
  for f in funcs:
    if f == 'do()':
      do = True
    elif f == 'don\'t()':
      do = False
    elif do:
      x, y = map(int, re.findall(r'\d{1,3}', f))
      ans += mul(x, y)

print(ans)