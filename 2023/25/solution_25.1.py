import networkx as nx
import matplotlib.pyplot as plt
import mplcursors

input = open('./input_25.txt', 'r')
lines = input.readlines()
L = [line.replace(':', '').strip().split(' ') for line in lines]

G = {}
for l in L:
  u = l[0]
  if u not in G:
    G[u] = []
  for v in l[1:]:
    G[u].append(v)
    if v not in G:
      G[v] = [u]
    else:
      G[v].append(u)

PLOT = False
if PLOT:
  graph = nx.from_dict_of_lists(G)

  pos = nx.spring_layout(graph)
  nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=100, node_color='skyblue', font_color='black', font_size=10, edge_color='gray')

  def edge_hover(sel):
      source, target = sel.target
      label = f"{source} -> {target}"
      sel.annotation.set_text(label)

  edges = [(node1, node2) for node1, node2 in graph.edges()]
  for edge in edges:
      graph[edge[0]][edge[1]]['label'] = f"{edge[0]} -> {edge[1]}"

  mplcursors.cursor(hover=True).connect("add", edge_hover)

  plt.show()
else:
  E = [('cvx', 'dph'), ('pzc', 'vps'), ('sgc', 'xvk')]
  for u, v in E:
    G[u].remove(v)
    G[v].remove(u)
  
  vis = set()
  def walk(i):
    if i in vis:
      return 0
    vis.add(i)

    cnt = 1
    for j in G[i]:
      cnt += walk(j)

    return cnt
  
  sets = []
  for i in G.keys():
    if i in vis:
      continue
    sets.append(walk(i))
  
  print(sets)
  res = sets[0] * sets[1]
  print(res)
