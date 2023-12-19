import copy


input = open('./input_19.txt', 'r')
lines = [line.split() for line in input.read().split('\n\n')]

R = {l[0]: l[1][:-1].split(',') for l in [l.split('{') for l in lines[0]]}

START = 'in'
ACCEPTED = 'A'
REJECTED = 'R'
MAX = 4000

M = [[(0, MAX) for _ in range(4)] for _ in range(len(R.keys()))]

def calc_ways(parts):
  ways = 1
  for v in parts.values():
    l = v[0]
    h = v[1]
    if l >= h:
      return 0
    ways *= (h-l+1)
  return ways

def rec(curr, parts):
  res = 0
  newcurr = R[curr][-1]
  accepting = newcurr == ACCEPTED

  for r in R[curr][:-1]:
    i  = r.index(':')
    p = r[0]
    op = r[1]
    v = int(r[2:i])
    k = 0
    plus = 1
    if op == '<':
      k = 1
      plus = -1
    target = r[i+1:]

    partscopy = copy.deepcopy(parts)
    partscopy[p][k] = v+plus
    parts[p][abs(k-1)] = v
    if target == ACCEPTED:
      res += calc_ways(partscopy)
    elif target != REJECTED:
      res += rec(target, partscopy)

  if accepting:
    res += calc_ways(parts)
  elif not newcurr == REJECTED:
    res += rec(newcurr, parts)

  return res

res = rec(START, {'x': [1, MAX], 'm': [1, MAX], 'a': [1, MAX], 's': [1, MAX]})
print(res)
