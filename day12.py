
def build_graph(pipes):
  G = {}
  for pipe in pipes:
    node, children = parse_pipe(pipe)
    G[node] = children
  return G


def parse_pipe(pipe):
  node, children = pipe.split("<->")

  node = int(node.strip())
  children = map(int, children.strip().split(","))
  return (node,children) 

def explore_from(u, G):
  queue = [u]
  visited = set()
  while queue:
    x = queue.pop(0)
    visited.add(x)
    for v in G[x]:
      if v not in visited:
        queue.append(v)
  return visited

def number_of_groups(G):
  data = {}
  data['visited'] = set()
  data['groups'] = 0 
  
  def dfs(u, G):
    data['visited'].add(u)
    for v in G[u]:
      if v not in data['visited']:
        dfs(v, G)
  
  for x in G:
    if x not in data['visited']:
      dfs(x,G)
      data['groups'] += 1

  return data['groups']
    


if __name__ == "__main__":
  
  FILENAME = 'pipes'
  with open(FILENAME, 'r') as f:
    G = build_graph(f.readlines())

  print "part I:"
  print "  programs in 0-group: ", len(explore_from(0, G))

  print "\npart II:"
  print "  programs groups: ", number_of_groups(G)
