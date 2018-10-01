

def parse_tower(t):
  if t.find("->") > -1:
    ancestor, children = t.replace(" ", "").split("->")
    name, weight = ancestor.split("(")
    return {
      'node': name,
      'weight': int(weight[:-1]),
      'children': set(children.strip().split(","))
    }
  else:
    name, weight = t.strip().replace(" ", "").split("(")
    return {
      'node': name,
      'weight': int(weight[:-1]),
      'children': set()
    }

def topo_sort(G):
  d = {}
  d['seen'] = set()
  d['topo'] = []

  def dfs(G, u):
    d['seen'].add(u)
    for child in G[u]['children']:
      if child not in d['seen']:
        dfs(G, child) 
    d['topo'].insert(0, u)

  for x in G:
    if x not in d['seen']:
      dfs(G, x)
  return d['topo']

def balance_weights(ts, G):
  for node in reversed(ts):
    G[node]['cweight'] = G[node]['weight']
    weights = []
    children = []
    for v in G[node]['children']:
      w = G[v]['cweight'] 
      if len(weights) > 1 and w != weights[-1]:
        if w == weights[0]:
          wrong = weights[-1]
          wchild= children[-1]
          dif = w - wrong
          print '{} has wrong weight: {}'.format(wchild, wrong)
          G[wchild]['weight'] += dif 
          print 'new weight', G[wchild]['weight']
          weights[-1] = w
        else:
          right = weights[0]
          dif = right - w
          G[v]['weight'] += dif 
          print 'setting \'{}\' weight to \'{}\' to balance weights'.format(v, G[v]['weight'])
          w = right

      weights.append(w)
      children.append(v)

    if len(set(weights)) <= 1:
      G[node]['cweight'] = G[node]['weight'] + sum(weights)
      
    
  
  
if __name__ == "__main__":
  T = {}
  with open("towers", "r") as f:
    for line in f.readlines():
      p = parse_tower(line)
      T[p['node']] = {'children': p['children'], 'weight': p['weight']}


  tp = topo_sort(T)
  print tp[0]

  balance_weights(tp, T)
