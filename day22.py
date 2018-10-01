from collections import defaultdict

def make_grid(grid_start, n=100):
  if len(grid_start) != len(grid_start[0]):
    print r"Must be 'NxN' grid."  
    return grid_start
  if n % 2 != 0:
    print r"Only handling even 'n'."
    return grid_start

  G = []
  grid_length = len(grid_start)     ## assume NxN grid

  G = [['.' for _ in range(grid_length+n)] for _ in range(n/2)]
  for i in range(grid_length):
    start,end = ['.' for _ in range(n/2)], ['.' for _ in range(n/2)]
    middle = list(grid_start[i])
    G.append(start + middle + end)

  for _ in range(n/2):
    G.append(['.' for _ in range(grid_length+n)])

  return G

def parse_grid(G):
  d = defaultdict(int)
  for i in range(len(G)):
    for j in range(len(G)):
      if G[i][j] == '#':
        d[(i,j)] = 1
      else:
        d[(i,j)] = 0
  return d

def traverse(G, iters=5):
  i,j = (len(G)/2, len(G)/2)
  facing = "N"
  c = 0

  for _ in range(iters):
    infected = G[i][j] == '#'
    if infected: ## go right
      G[i][j] = '.'
      if facing == "N":
        j+=1
        facing = "E"
      elif facing == "S":
        j-=1
        facing = "W"
      elif facing == "E":
        i+=1
        facing = "S"
      elif facing == "W":
        i-=1
        facing = "N"
    else:        ## go left
      c+=1
      G[i][j] = '#'
      if facing == "N":
        j-=1
        facing = "W"
      elif facing == "S":
        j+=1
        facing = "E"
      elif facing == "E":
        i-=1
        facing = "N"
      elif facing == "W":
        i+=1
        facing = "S"
  return c

def traverse2(D, iters=5):
  i,j = 12, 12
  facing = "N"
  c = 0

  for _ in range(iters):
    infected = D[(i,j)]
    if infected: ## go right
      D[(i,j)] = 0
      if facing == "N":
        j+=1
        facing = "E"
      elif facing == "S":
        j-=1
        facing = "W"
      elif facing == "E":
        i+=1
        facing = "S"
      elif facing == "W":
        i-=1
        facing = "N"
    else:        ## go left
      c+=1
      D[(i,j)] = 1
      if facing == "N":
        j-=1
        facing = "W"
      elif facing == "S":
        j+=1
        facing = "E"
      elif facing == "E":
        i-=1
        facing = "N"
      elif facing == "W":
        i+=1
        facing = "S"
  return c


def traverse3(D, iters=5, i=12, j=12):
  facing = "N"
  c = 0
  ## state diagram
  ## clean->weakened->infected => 0 -> 2 -> 1
  ## infected->flagged->clean  => 1 -> -1 -> 0

  for _ in range(iters):
    infected = D[(i,j)] == 1
    clean = D[(i,j)] == 0
    weakened = D[(i,j)] == 2
    flagged = D[(i,j)] == -1

    if infected:          ## go right
      D[(i,j)] = -1
      if facing == "N":
        j+=1
        facing = "E"
      elif facing == "S":
        j-=1
        facing = "W"
      elif facing == "E":
        i+=1
        facing = "S"
      elif facing == "W":
        i-=1
        facing = "N"
    elif weakened:        ## does not turn
      c+=1
      D[(i,j)] = 1
      if facing == "N":
        i-=1
      elif facing == "S":
        i+=1
      elif facing == "E":
        j+=1
      elif facing == "W":
        j-=1
    elif flagged:
      D[(i,j)] = 0
      if facing == "N":
        i+=1
        facing = "S"
      elif facing == "S":
        i-=1
        facing = "N"
      elif facing == "E":
        j-=1
        facing = "W"
      elif facing == "W":
        j+=1
        facing = "E"
    elif clean:           ## go left
      D[(i,j)] = 2
      if facing == "N":
        j-=1
        facing = "W"
      elif facing == "S":
        j+=1
        facing = "E"
      elif facing == "E":
        i-=1
        facing = "N"
      elif facing == "W":
        i+=1
        facing = "S"
  return c

if __name__ == "__main__":

  with open("virus", "r") as f:
    GG = map(lambda x: x.strip('\n'), f.readlines())

  D = parse_grid(GG)
  c = traverse2(D, iters=10000)

  print "part I:"
  print "  infected: ", c

  D = parse_grid(GG)
  c = traverse3(D, iters=10000000) 

  print "\npart II:"
  print "  infected: ", c
