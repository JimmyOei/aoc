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

PUSHES = 1000

low = PUSHES
high = 0
for _ in range(PUSHES):
  curr = [(False, i, None) for i in start]
  while len(curr) > 0:
    pulse, c, prev = curr.pop(0)
    if pulse:
      high += 1
    else:
      low += 1

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
res = low * high
print(res, low, high)
