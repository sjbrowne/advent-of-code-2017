
def go_one(n):
  lim = n 
  n = 0
  while n < lim: 
    yield c
    n+=1

def generator(seed,factor):
  tmin = 1<<31;
  prev = seed
  while True: 
    nxtv = (prev*factor)%(tmin-1) 
    yield nxtv 
    prev = nxtv

def generator3(seed,factor,mult):
  prev = seed
  while True: 
    g = generator(prev, factor)
    nxtv = next(g)
    while nxtv % mult != 0:
      nxtv = next(g)
    yield nxtv 
    prev = nxtv



def bitmatch(x,y,mask):
  return (x & mask) ^ (y & mask) == 0

if __name__ == "__main__": 
  SHOULD_RUN = True
  if SHOULD_RUN: 
    seed_a, seed_b = 679, 771 
    factor_a, factor_b = 16807, 48271 
    a,b = generator(seed_a, factor_a), generator(seed_b, factor_b)

    mask = 1<<15 
    mask = mask | mask >> 1
    mask = mask | mask >> 2
    mask = mask | mask >> 4
    mask = mask | mask >> 8

    c = 0
    for i in xrange(40000000):
      x,y = next(a), next(b)
      if bitmatch(x,y,mask):
        c += 1

    print 'part I:'
    print '  16-bit matches:', c

    c = 0
    aa,bb = generator3(seed_a, factor_a, 4), generator3(seed_b, factor_b, 8)
    for i in xrange(5000000):
      x,y  = next(aa), next(bb)
      if bitmatch(x,y, mask):
        c += 1

    print '\npart II:'
    print '  16-bit matches:', c
  else:
    print 'Change \'SHOULD_RUN\' to \'True\'.\nWARNING: Running time > 1 min.'

    
      
