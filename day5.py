
def readjumps(filename):
  f = open(filename,'r')
  return map(lambda l: int(l.strip()), f.readlines())

def jumps(a):
  i,res = 0,0
  while i < len(a):
    res += 1
    tmp_i = i
    i += a[i]
    a[tmp_i] += 1
  return res

def jumps2(a):
  i,res = 0,0
  while i < len(a):
    res += 1
    tmp_i = i
    i += a[i]
    a[tmp_i] = a[tmp_i]+1 if a[tmp_i] < 3 else a[tmp_i]-1
  return res


if __name__ == "__main__":
 a = readjumps("jumps")
 print "part I:"
 print "  inc:     ", jumps(a)

 a = readjumps("jumps")
 print "\npart II:"
 print "  inc/dec: ", jumps2(a)
