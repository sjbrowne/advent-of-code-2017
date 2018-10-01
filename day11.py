import heapq as hq

def get_move(key):
   movetype = { 
     "skip" : {
       "ne" : (1,  1),
       "se" : (1, -1),
       "nw" : (-1, 1), 
       "sw" : (-1, -1),
       "n"  : (0,   2),
       "s"  : (0,  -2)
     },
     "rgrain" : {
       "ne" : (1,  0),
       "se" : (1, -1),
       "nw" : (-1, 1), 
       "sw" : (-1, 0),
       "n"  : (0,  1),
       "s"  : (0, -1)
     }
   }
   return movetype[key] 
  

def man_dist(start, goal):
  dx = abs(start[0] - goal[0])
  yprime = start[1] - dx if start[1] > goal[1] else start[1] + dx
  return dx + abs(yprime - goal[1])/2
  
def man_dist2(start, goal):
  x1, y1 = start
  x2, y2 = goal

  dx = x2 - x1 if x2 >= x1 else x1 - x2
  dy = y2 - y1 if y2 >= y1 else y1 - y2
  #print 'dx', dx 
  #print 'dy', dy 
  if dy < dx:
    return dx
  if y1 == y2: return dx
  yprime = y1 + dx if y1 <= y2 else y1 - dx 
  #print 'yprime', yprime
  #print 'sub', max((yprime - y2)/2 - 2, 0)
  return dx + abs(yprime - goal[1])/2

def man_dist3(start, goal):
  x1, y1 = start
  x2, y2 = goal

  dx = x2 - x1 if x2 >= x1 else x1 - x2
  dy = y2 - y1 if y2 >= y1 else y1 - y2
  return dy + dx
  


def get_coords(path):
  x,y = 0,0
  move = get_move("rgrain") 

  for dirctn in path.split(","):
    dx,dy = move[dirctn]
    x += dx
    y += dy

  return (x,y)

def get_inter_coords(path):
  x,y = 0,0
  move =  get_move("rgrain")

  coords = []
  for dirctn in path.split(","):
    dx,dy = move[dirctn]
    x += dx
    y += dy
    coords.append((x,y))
  return coords
    
  


def search(start, goal):
  move = get_move("rgrain")

  visited = set()

  queue = [(0,start[0],start[1])]
  steps, steps_max = 0,0

  while queue:
    s,x,y = queue.pop(0)

    if (x,y) == goal:
      return s

    for child in move:
      dx,dy = move[child]
      candidate = (x+dx, y+dy)
      if candidate not in visited:
        queue.append((s+1, x+dx, y+dy))
        visited.add(candidate)

  print "Could could not be reached."
  return None

def astar(start, goal):
  move = get_move("rgrain")

  visited = set()

  cost = man_dist2(start, goal)
  queue = [(cost,0,start[0],start[1])]
  hq.heapify(queue)

  while queue:
    c,s,x,y = hq.heappop(queue)

    if (x,y) == goal:
      return s

    for child in move:
      dx,dy = move[child]
      candidate = (x+dx, y+dy)
      if candidate not in visited:
        hq.heappush(queue, (s+1+man_dist2(candidate, goal), s+1, x+dx, y+dy))
        visited.add(candidate)

  print "Could could not be reached."
  return None


if __name__ == "__main__":
  from random import randint

  with open("steps", "r") as f:
    path = f.readline().strip()

  coords = get_coords(path) 
  print "part I: "
  print "  coords: ", coords
  #steps = search((0,0,0), get_coords(path))
  print "  steps: ", man_dist3((0,0), coords)

  M = 0
  MS = []
  allcoords = get_inter_coords(path)
  for start in allcoords:
    #steps = man_dist2(start, coords) 
    steps = man_dist3(start, coords) 
    if steps > M: 
      M = steps
    MS.append((steps, start[0], start[1]))

  print "\npart II:"
  print "  max dist: ", M
  
  evens = range(-1000,1000,2)
  odds  = range(-1001,1000,2)
  for _ in range(100):
    x1, x2 = evens[randint(0,len(evens)-1)], evens[randint(0,len(evens)-1)]  
    y1, y2 = odds[randint(0,len(odds)-1)], odds[randint(0,len(odds)-1)]  
    start,goal = (x1, y1),(x2, y2)
    ss,mm = astar(start,goal), man_dist3(start,goal)
    #ss,mm = search(start,goal), man_dist(start,goal)
 
    if ss != mm: 
      print "INCORRECT!!! {} should be {}".format(mm, ss)
    else:
      print "CORRECT! ({}) -> ({}) : ({})".format(start, goal, mm)
 

