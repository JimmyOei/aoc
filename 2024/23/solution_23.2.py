import networkx as nx
import matplotlib.pyplot as plt

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
    
G = nx.Graph()
for k in mp.keys():
  for neighbor in mp[k]:
    G.add_edge(k, neighbor)
nx.draw(G, with_labels=True)
plt.show()

# ans = ["ob", "ji", "dy", "ka", "qv", "ry", "xz", "ef", "jv", "ua", "wt", "iw", "cw"]
# >>> ans
# ['ob', 'ji', 'dy', 'ka', 'qv', 'ry', 'xz', 'ef', 'jv', 'ua', 'wt', 'iw', 'cw']
# >>> ans.sort()
# >>> ans
# ['cw', 'dy', 'ef', 'iw', 'ji', 'jv', 'ka', 'ob', 'qv', 'ry', 'ua', 'wt', 'xz']
# >>> ",".join(ans)
# 'cw,dy,ef,iw,ji,jv,ka,ob,qv,ry,ua,wt,xz'