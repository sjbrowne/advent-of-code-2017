from collections import defaultdict

def findSquare(n):
  a = 1
  while a**2 < n and a < 1e9:
    a+=2
  return a

def computeLeg(n, s):
  return (s**2 - n)/(s-1) 

def computeMod(n, s):
  return (s**2 - n) % (s-1)

## NOTE
## origin is at the square corner (bottom right), positive y is up and 
## positive x is left
def countSteps(n):
  if n == 1: return 0
  s = findSquare(n)
  leg = computeLeg(n, s)
  rc  = computeMod(n, s) 
  if leg == 0:
    coords = (0,  rc)
  if leg == 1:
    coords = (rc,s-1)
  if leg == 2:
    coords = (s-1, s-1-rc)
  if leg == 3:
    coords = (s-1-rc,   0)
  return abs(s/2 - coords[0]) + abs(s/2 - coords[1])

def sum_spiral(M):
  d = defaultdict(int)
  xsteps, ysteps = 1, -1 
  x,y = 0,0
  c = 0
  d[(0,0)] = 1
  while True:
    if x < (x + xsteps):                  ## right
      for i in range(x, x + xsteps+1):
        if d[(i,y)] == 0:
          left = (i-1, y)
          up = (i, y-1)
          lup = (i-1, y-1) 
          rup = (i+1, y-1)
          s = d[left] + d[up] + d[rup] + d[lup]
          d[(i,y)] = s
          c += 1
          if s > M: return s
    elif x > (x + xsteps):                ## left
      for i in range(x, x + xsteps - 1, -1):
        if d[(i,y)] == 0:
          right = (i+1, y)
          down  = (i, y+1)
          rdown = (i+1, y+1) 
          ldown = (i-1, y+1)
          s = d[right] + d[down] + d[rdown] + d[ldown]
          d[(i,y)] = s
          c += 1
          if s > M: return s  

    x += xsteps

    if y < (y + ysteps):                  ## down
      for i in range(y, y + ysteps):
        if d[(x,i)] == 0:
          up = (x, i-1)
          right = (x+1, i)
          rup = (x+1, i-1)
          rdown = (x+1, i+1)
          s = d[up] + d[right] + d[rup] + d[rdown]
          d[(x,i)] = s
          c += 1
          if s > M: return s
    elif y > (y + ysteps):                ## up 
      for i in range(y, y + ysteps-1, -1):
        if d[(x,i)] == 0:
          down = (x, i+1)
          left = (x-1, i)
          lup  = (x-1, i-1)
          ldown = (x-1, i+1)
          s = d[down] + d[left] + d[lup] + d[ldown]
          d[(x,i)] = s
          c += 1
          if s > M: return s 

    y += ysteps
    xsteps =  (-1)*xsteps + 1 if xsteps < 0 else (xsteps + 1)*(-1)
    ysteps =  (-1)*ysteps + 1 if ysteps < 0 else (ysteps + 1)*(-1)

  return d
    

if __name__ == "__main__":
  
  print "part I:"
  print "  distance to origin:", countSteps(312051)

  print "\npart II:"
  print "  first value over 312051:", sum_spiral(312051)
