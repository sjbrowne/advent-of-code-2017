## NOTES 
## https://www.redblobgames.com/grids/hexagons/

def get_move(key):
   up,dn,st = 1,-1,0
   movetype = { 
     "cube" : {
       "ne" : (up, st, dn),
       "sw" : (dn, st, up),
       "nw" : (dn, up, st), 
       "se" : (up, dn, st),
       "n"  : (st, up, dn),
       "s"  : (st, dn, up)
     }
   }
   return movetype[key] 


def get_coords(path):
  move = get_move("cube")
  x,y,z = 0,0,0
  
  for dirctn in path.split(","):
    dx,dy,dz = move[dirctn]
    x += dx
    y += dy
    z += dz

  return (x,y,z)


def find_max(path, goal):
  move = get_move("cube")
  x,y,z = 0,0,0
  M = 0 
  
  for dirctn in reversed(path.split(",")):
    dx,dy,dz = move[dirctn]
    x += dx
    y += dy
    z += dz
    m = man_distance((x,y,z), goal)
    if m > M: M = m

  return M 

def man_distance(start, goal):
  return max(map(lambda (x,y): abs(x-y), zip(start, goal)))


if __name__ == "__main__":
  
  with open("steps", "r") as f:
    path = f.readline().strip()

  start= (0,0,0)
  goal = get_coords(path)
  print "part I: "
  print "  goal:     ", goal
  print "  distance: ", man_distance(start, goal)

  print "\npart II: "
  print "  max:      ", find_max(path, goal)
