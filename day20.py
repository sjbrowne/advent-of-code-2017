import re
from collections import defaultdict

def mandist(p, key='p'):
  return sum(map(abs, p[key]))

def parse_particle(praw):
  attrs = map(int, filter(bool, re.findall(r"-[0-9]*|[0-9]*", praw)))
  px,py,pz = attrs[0:3]
  vx,vy,vz = attrs[3:6]
  ax,ay,az = attrs[6:]
  p = {
    "p": (px,py,pz),
    "v": (vx,vy,vz),
    "a": (ax,ay,az)
  }
  return p

def min_val(particles, attr='a'):
  amin = [1e9, None]
  for i,p in enumerate(particles):
    a = mandist(p, key=attr)
    if a < amin[0]: 
      amin[0] = a
      amin[1] = i
  return amin

def min_val_l(particles, attr='a'):
  amin = [1e9, None]
  vals = []
  for i,p in enumerate(particles):
    a = mandist(p, key=attr)
    if a < amin[0]: 
      amin[0] = a
      amin[1] = i
      vals = [tuple(amin)]
    elif a == amin[0]:
      vals.append((amin[0],i))
  return vals

def simulate(P, iterations=1000):
  for _ in range(iterations):
    for i in range(len(P)):

      dv = map(sum, zip(P[i]['v'], P[i]['a']))
      P[i]['v'] = tuple(dv) 

      dp = map(sum, zip(P[i]['p'], P[i]['v']))
      P[i]['p'] = tuple(dp)


def simulate_collisions(P, iterations=1000):
  for _ in range(iterations):
    i = 0
    positions = defaultdict(list)

    while i < len(P):
      dv = map(sum, zip(P[i]['v'], P[i]['a']))
      P[i]['v'] = tuple(dv) 

      dp = map(sum, zip(P[i]['p'], P[i]['v']))
      P[i]['p'] = tuple(dp)

      positions[P[i]['p']].append(i)

      i+=1

    pop_list = []
    for p in positions:
      if len(positions[p]) > 1:
        pop_list += positions[p]

    popped = 0
    for pi in sorted(pop_list):
      P.pop(pi-popped)
      popped+=1
    

if __name__ == "__main__":
  big = "particles"

  SIMULATE = False

  with open(big, 'r') as f:
    particles = map(lambda x: x.strip("\n"), f.readlines())

  P = []
  for praw in particles:
    p = parse_particle(praw)
    P.append(p)

  ## find smallest acceleration
  accel_mins = min_val_l(P)

  ## find the closest to the origin of mins
  m,mi = 1e9, None
  for x in accel_mins:
    amin_d = mandist(P[x[1]], key='p')
    if amin_d < m:
      m = amin_d
      mi = x[1]

  print 'part I: '
  print '  closest particle: ', mi

  simulate_collisions(P, iterations=100)

  print '\npart II: '
  print '  particles remaining: ', len(P)
      

  if SIMULATE:

    a,ai = min_val(P)
    d,di = min_val(P, attr='p')
    v,vi = min_val(P, attr='v')

    print 'a', a,ai
    print 'd', d,di
    print 'v', v,vi

    simulate(P)

    a,ai = min_val(P)
    d,di = min_val(P, attr='p')
    v,vi = min_val(P, attr='v')

    print '\na', a,ai
    print 'd', d,di
    print 'v', v,vi

    simulate(P)

    a,ai = min_val(P)
    d,di = min_val(P, attr='p')
    v,vi = min_val(P, attr='v')

    print '\na', a,ai
    print 'd', d,di
    print 'v', v,vi
