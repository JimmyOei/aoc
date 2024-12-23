input = open('./input_23.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

mp = {}

for line in lines:
  nodes = line.split('-')
  if nodes[0] in mp:
    mp[nodes[0]].append(nodes[1])
  else:
    mp[nodes[0]] = [nodes[1]]
  if nodes[1] in mp:
    mp[nodes[1]].append(nodes[0])
  else:
    mp[nodes[1]] = [nodes[0]]

setlength = 3
validsets = []
for k in mp.keys():
  if k.startswith('t'):
    q = [(k, [k])]
    for _ in range(setlength-1):
      qlength = len(q)
      for _ in range(qlength):
        node, path = q.pop(0)
        for neighbor in mp[node]:
          if neighbor not in path:
            q.append((neighbor, path + [neighbor]))
    for node, path in q:
      neighbors = mp[node]
      path.sort()
      if k in neighbors and path not in validsets:
        validsets.append(path)
ans = len(validsets)
print(ans)