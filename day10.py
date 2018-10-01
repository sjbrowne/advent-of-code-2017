def convert_to_blocks(a, size):
  if len(a) % size != 0:
    print "Does not divide equally. Returning."
    return a
  i,j,l = 0,size,[]
  for i in range(1, len(a)/size + 1):
    start,end = (i-1)*size, i*size
    l.append(a[start:end])
  return l
  
def xor_block(nums):
  return reduce(lambda x,y: x^y, nums,0)

def ascii_to_hex(x):
  return hex(x).replace('0x', '').zfill(2)

def str_to_ascii(s):
  return map(ord, s)
  
def swap(l,i,j):
  jj = j%len(l)
  l[i],l[jj] = l[jj],l[i]

def reverse(l, start, ln):
  end = start + (ln/2)
  for off,i in enumerate(range(start, end)):
    swap(l, i%len(l), start + ln - 1 - off)

def knothash(lengths, l=256):
  s,i,a = 0,0,range(l)
  for ln in lengths:
    reverse(a, i, ln)
    i=(i+ln+s)%l
    s+=1
  return a

def knothashr(S, l=256, rounds=1):
  tail = [17, 31, 73, 47, 23]
  L = str_to_ascii(S) + tail
  lengths = []
  while rounds > 0:
    lengths += L
    rounds -= 1

  s,i,a = 0,0,range(l)
  for ln in lengths:
    reverse(a, i, ln)
    i=(i+ln+s)%l
    s+=1

  return ''.join(map(ascii_to_hex, map(xor_block, convert_to_blocks(a, 16))))




if __name__ == "__main__":
  input = [106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118]

  res = knothash(input)
  print "part I:  ", res[0]*res[1]

  lengths = ",".join(map(str,input))
  print "part II: ", knothashr(lengths, rounds=64)
