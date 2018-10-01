class Port(object):

  id = 0 
  def __init__(self, port_raw, id=None):
    self.p1, self.p2 = map(int, port_raw.split('/'))
    self.p1conn = False
    self.p2conn = False
    self.neighbors = set()
    self._id = Port.id if not id else id
    Port.id+=1

  def add_neighbor(self, other):
    self.neighbors.add(other)
    
  def sum(self):
    return self.p1 + self.p2

  def has_zero_port(self):
    return self.p1 == 0 or self.p2 == 0

  def can_connect(self, other):
    if self == other:
      return -1
    if (self.p1 == other.p1) or (self.p1 == other.p2):
      if not self.p1conn:
        return self.p1
    if (self.p2 == other.p1) or (self.p2 == other.p2):
      if not self.p2conn:
        return self.p2
    return -1
    
  def connect_port(self, pins):
    if pins == self.p1:
      self.p1conn = True
    elif pins == self.p2:
      self.p2conn = True
    else:
      print 'ERR: Cannot connect', self

  def disconnect_port(self, pins):
    if pins == self.p1 and self.p1conn:
      self.p1conn = False
    elif pins == self.p2 and self.p2conn:
      self.p2conn = False
    else:
      #print 'ERR: Cannot disconnect {} from'.format(pins), self
      pass

  def reset(self):
    self.p1conn = False
    self.p2conn = False

  def __lt__(self,other):
    return sum([self.p1, self.p2]) < sum([other.p1, other.p2])

  def __eq__(self,other):
    return sum([self.p1, self.p2]) == sum([other.p1, other.p2])

  def __str__(self):
    p1c = 'connected' if self.p1conn else 'open'
    p2c = 'connected' if self.p2conn else 'open'

    return "[{}] p1: {} ({}) p2: {} ({}) ".format(self._id, self.p1, p1c, self.p2, p2c)


def pl(zero, pdict):
  stack = set()
  zero.connect_port(0)
  smax = {'len':0, 'val':0}
  def path_length(node):
    stack.add(node._id)
    m, c = 0, 0
    for nei in node.neighbors: 
      if nei._id not in stack:
        conn = node.can_connect(nei)
        if conn > -1:
          node.connect_port(conn)
          nei.connect_port(conn)
          c = path_length(nei)
          if c > m: m = c
          node.disconnect_port(conn)
          nei.disconnect_port(conn)

    if len(stack) > smax['len']: 
      smax['val'] = sum(map(lambda x: pdict[x].sum(), stack))
      smax['len'] = len(stack)
    elif len(stack) == smax['len']:
      s = sum(map(lambda x: pdict[x].sum(), stack))
      if s > smax['val']: smax['val'] = s
      
    stack.remove(node._id)
    return node.sum()+m 

  m = path_length(zero)

  return (m,smax['val'])

if __name__ == "__main__":
  big, small, small2 = 'ports', 'ports_small', 'ports_small2' 

  with open(big, 'r') as f:
    plist = [ Port(p.strip()) for p in f.readlines()]

  pdict = {}
  for port in plist:
    pdict[port._id] = port

  for p in plist:
    for i in range(len(plist)):
      if p.can_connect(plist[i]) >= 0:
        plist[i].add_neighbor(p)
        p.add_neighbor(plist[i])

  zeros = [p if p.has_zero_port() else None for i,p in enumerate(plist)]
  zeros = filter(bool, zeros)

  res = pl(zeros[1], pdict)
  print "part I: "
  print "  strongest bridge: ", res[0] 

  print "\npart II: "
  print "  strongest, longest bridge: ", res[1] 

  #M = [pl(z,pdict) for z in zeros]
  
