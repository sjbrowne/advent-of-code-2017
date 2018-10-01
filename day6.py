

def blocks(a):
  seen = set()
  res = 0
  while tuple(a) not in seen: 
    seen.add(tuple(a))
    res += 1
    i = a.index(max(a))
    s, a[i]  = a[i], 0
    i+=1
    while s > 0:
      a[i%len(a)] += 1
      s -= 1
      i += 1
  return res

if __name__ == "__main__":
  a = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]

  print "part I:"
  print "  redistribution cycles: ", blocks(a)

  ## start with the looping distribution to get the cycle length
  ## a is modified in place, so redo routine on the current a
  print "\npart II:"
  print "  loop size: ", blocks(a)
