

def valid(s):
  S = set()
  for x in s.strip().split(" "):
    if x in S: return False
    S.add(x)
  return True

def validana(s):
  S = set()
  ss = map(sorted, s.strip().split(" "))
  for x in map(lambda x: str.join('', x), ss):
    if x in S: return False
    S.add(x)
  return True
  

if __name__ == "__main__":
  c,d = 0,0
  a = []
  with open("passphrases", "r") as f:
    for i,line in enumerate(f.readlines()):
      if valid(line):
        c+=1
        a.append(i)
      if validana(line):
        d+=1

  print 'part I:'
  print '  valid phrases: ', c

  print '\npart II:'
  print '  valid phrases: ', d
