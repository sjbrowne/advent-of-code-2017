from day10 import knothashr 

def hash_to_bin(h):
  b = ''
  for x in h:
    b += bin(int(x, 16))[2:].zfill(4)
  return b

def count_regions(B):
  
  data = {}
  data['visited'] = set()
  def dfs(i,j,B):
    data['visited'].add((i,j))
    if i>=0 and i<len(B) and \
       j>=0 and j<len(B[0]):
       if B[i][j] == '1':
         if (i+1, j) not in data['visited']:
           dfs(i+1,j,B)
         if (i-1, j) not in data['visited']:
           dfs(i-1,j,B)
         if (i, j+1) not in data['visited']:
           dfs(i,j+1,B)
         if (i, j-1) not in data['visited']:
           dfs(i,j-1,B)

  regions = 0
  for i in range(len(B)):
    for j in range(len(B[0])):
      if (i,j) not in data['visited'] and B[i][j] == '1':
        regions += 1
        dfs(i,j,B)
  return regions
      
  

if __name__ == "__main__":
  h = "hxtvlmkl-"
  hs = []
  for i in range(128):
    hs.append( knothashr(h+str(i), rounds=64) )

  bh = map(hash_to_bin, hs)
  bn = map(lambda x: x.count('1'), bh)

  print "part I:"
  print "  squares used: ", sum(bn)
  
  print "part II:"
  print "  regions: ", count_regions(bh)
