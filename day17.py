

def spinlock(lim,steps):
  a = [0]
  i,c = 0, 1  
  while c < lim:
    i = (i+steps) % len(a)
    a.insert(i+1, c)
    i = i+1
    c+=1
  return a


def spinlock0(lim,steps):
  i,c,l = 0, 1, 1 
  z = 0
  while c < lim:
    i = (i+steps) % l
    if i == 0:
      z = c
    l+=1 
    i = i+1
    c+=1
  return z

if __name__ == "__main__":
  res = spinlock(2018,345)

  print "part I:"
  print "  value after 2017: ", res[res.index(2017)+1]

  z = spinlock0(50000001,345)

  print "\npart II:"
  print "  value @1 after 50M: ", z
