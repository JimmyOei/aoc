input = open('./input_19.txt', 'r')
lines = [line.split() for line in input.read().split('\n\n')]

R = {l[0]: l[1][:-1].split(',') for l in [l.split('{') for l in lines[0]]}
P = [tuple(int(p[2:]) for p in l[1:-1].split(',')) for l in lines[1]]

START = 'in'
ACCEPTED = 'A'
REJECTED = 'R'

res = 0
for x, m, a, s in P:
  curr = START
  while curr != ACCEPTED and curr != REJECTED:
    newcurr = R[curr][-1]
    for r in R[curr][:-1]:
      i  = r.index(':')

      if eval(r[:i]):
        newcurr = r[i+1:]
        break
    curr = newcurr
  if curr == ACCEPTED:
    res += sum([x, m, a, s])
print(res)
