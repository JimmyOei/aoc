import math

input = open('./input_20.txt', 'r')
lines = input.readlines()

start = None
F = {}
I = {}
S = {}
for l in lines:
  i = l.index('-')
  if l[0] == '%':
    node = l[1:i].strip()
    F[node] = l[i+3:].strip().split(', ')
    S[node] = False
  elif l[0] == '&':
    node = l[1:i].strip()
    I[node] = ({}, l[i+3:].strip().split(', '))
    S[node] = False
  else:
    start = l[i+3:].strip().split(', ')

for k, v in F.items():
  for i in v:
    if i in I:
      I[i][0][k] = False

inv_rx = None
for i, v in I.items():
  if 'rx' in v[1]:
    inv_rx = i
    break

to_inv_rx = []
for i, v in I.items():
  if inv_rx in v[1]:
    to_inv_rx.append(i)
for i, v in F.items():
  if inv_rx in v:
    to_inv_rx.append(i)

its = []
steps = 0
while len(to_inv_rx) > 0:
  steps += 1
  curr = [(False, i, None) for i in start]
  while len(curr) > 0:
    pulse, c, prev = curr.pop(0)

    if prev in to_inv_rx and pulse:
      to_inv_rx.remove(prev)
      its.append(steps)

    if c in F:
      if not pulse:
        S[c] = not S[c]
        newpulse = S[c]
        for i in F[c]:
          curr.append((newpulse, i, c))
    elif c in I:
      I[c][0][prev] = pulse
      newpulse = True
      if all(I[c][0].values()) == True:
        newpulse = False
      for i in I[c][1]:
        curr.append((newpulse, i, c))

res = math.lcm(*(its))
print(res)
