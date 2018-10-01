
def spin(n,d,a): 
  i = (len(a)-n)
  for x in a[i:]:
    d[x] -= i
  for x in a[:i]:
    d[x] += n
  a = a[i:] + a[:i]
  return a


def swapi(i,j,d,a):
  x,y = a[i],a[j]
  a[i], a[j] = a[j], a[i]
  d[x] = j
  d[y] = i


def swapx(x,y,d,a):
  i,j = d[x], d[y]
  d[x],d[y] = j,i
  a[i],a[j] = a[j],a[i]


def programs(n):
  d,a = {},[]
  for i in range(n):
    d[chr(ord('a') + i)] = i 
    a += chr(ord('a') + i)
  return (d,a)


def dance(moves,n=16):
  a,d = programs(n)

  for move in moves:
    if move[0] == 's':
      n = int(move[1:])
      if n > 0:
        a = spin(n,d,a)
    elif move[0] == 'p':
      x,y = move[1:].split('/')
      swapx(x,y,d,a)
    elif move[0] == 'x':
      i,j = map(int,move[1:].split('/'))
      swapi(i,j,d,a)
    else:
      print 'ERROR! {} is not recognized'.format(move[0])
  return a

def dancex(moves,d,a):
  for move in moves:
    if move[0] == 's':
      n = int(move[1:])
      if n > 0:
        a = spin(n,d,a)
    elif move[0] == 'p':
      x,y = move[1:].split('/')
      swapx(x,y,d,a)
    elif move[0] == 'x':
      i,j = map(int,move[1:].split('/'))
      swapi(i,j,d,a)
    else:
      print 'ERROR! {} is not recognized'.format(move[0])
  return (d,a)


def test(a,d):
  for x in a:
    if a[d[x]] != x:
      print 'VIOLATION!!!'

if __name__ == "__main__":

  d,a = programs(16)
  with open('moves','r') as f:
    moves = f.readline().strip().split(",")
  d,res = dancex(moves,d,a)

  print "part I:"
  print "  program order: ", ''.join(res)

  one_bil = 1000000000
  one_mil = 1000000
  seen = {}
  skip = {}

  d,a = programs(16)

  ## brute i = 0
  ## brute while i < one_bil: 

  ## brute   if i / one_mil > 0 and i % one_mil < 100:
  ## brute     print 'i', i

  ## brute   h = ''.join(a)
  ## brute   if h not in seen:
  ## brute     d,a = dancex(moves,d,a)
  ## brute     seen[h] = ''.join(a)
  ## brute     skip[h] = [i, -1]
  ## brute     i+=1
  ## brute   elif skip[h][1] != -1:
  ## brute     i += skip[h][1]
  ## brute     a = list(seen[h])
  ## brute     for j in range(len(a)):
  ## brute       d[a[j]] = j 
  ## brute   else:
  ## brute     skip[h][1] = i 
  ## brute     a = list(seen[h])
  ## brute     for j in range(len(a)):
  ## brute       d[a[j]] = j 
  ## brute     i+=1

  i = 0
  while True:
    h = ''.join(a)
    if h not in seen:
      d,a = dancex(moves,d,a)
      seen[h] = ''.join(a)
      skip[h] = [i, -1]
    elif skip[h][1] != -1:
      i += skip[h][1]
      a = list(seen[h])
      for j in range(len(a)):
        d[a[j]] = j
    else:
      cycle = i
      m = one_bil % cycle
      for x in skip:
        skip[x][1] = skip[x][0] + cycle 
        if skip[x][0] == m:
          print '\npart II:'
          print '  program order: ', x 
      break
    i+=1

