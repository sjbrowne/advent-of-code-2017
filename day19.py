      
def traverse(pipes):
  LENi,LENj = len(pipes), len(pipes[0])

  i,j = 0,pipes[0].find("|")
  drctn = 'd' 
  nei = (i+1, j)
  s, steps = 1, []
  

  letters = []
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  L,U = set(alpha), set(alpha.upper())
  vert, hori = set('ud'), set('lr')

  while nei != None:
    i,j = nei

    node = pipes[i][j]
    nei = None
    s+=1

    if node == '+':
      steps.append(s)
      s = 0
      if drctn in hori:                        ## look u/d
        if i+1 < LENi and pipes[i+1][j] != ' ': 
          drctn = 'd'
          nei = (i+1, j)
        elif i-1 >= 0 and pipes[i-1][j] != ' ': 
          drctn = 'u'
          nei = (i-1, j)
      elif drctn in vert:                      ## look l/r
        if j+1 < LENj and pipes[i][j+1] != ' ': 
          drctn = 'r'
          nei = (i, j+1)
        elif j-1 >= 0 and pipes[i][j-1] != ' ': 
          drctn = 'l'
          nei = (i, j-1)
    else:
      if node in U or node in L:
        letters.append(node)

      if drctn == 'u':
        nei = (i-1, j) if i-1 >= 0 and pipes[i-1][j]   != ' ' else None
      if drctn == 'd':
        nei = (i+1, j) if i+1 < LENi and pipes[i+1][j] != ' ' else None
      if drctn == 'l': 
        nei = (i, j-1) if j-1 >= 0 and pipes[i][j-1]   != ' ' else None
      if drctn == 'r':
        nei = (i, j+1) if j+1 < LENj and pipes[i][j+1] != ' ' else None

  steps.append(s)
  return (''.join(letters), sum(steps))
 
   

if __name__ == "__main__":
  small, big = 'tubes_small', 'tubes'

  with open(big, 'r') as f:
    T = map(lambda x: x.strip('\n'), f.readlines())

  l,s = traverse(T)
  print "part I:"
  print "  letter order: ", l

  print "\npart II:"
  print "  steps: ", s 
