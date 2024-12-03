import re

def mul(x, y):
    return x * y

input = open('./input_03.txt', 'r')
lines = input.readlines()

ans = 0
for line in lines:
  muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
  for m in muls:
    x, y = map(int, re.findall(r'\d{1,3}', m))
    ans += mul(x, y)

print(ans)