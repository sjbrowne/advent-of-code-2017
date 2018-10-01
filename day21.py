

def divide(sq):
  x,y = shape(sq)
  TWO, THREE = 2,3

  if y != x:
    print "ERR(NOOP): Not expecting {} by {} square.".format(x,y)
    return sq

  if x % 2 == 0 and y % 2 == 0:
    WIDTH = TWO
  elif x % 3 == 0 and y % 3 == 0:
    WIDTH = THREE

  sql = sq.split("/")
  rows = []
  for row in range(0,x,WIDTH):
    new_row = []
    for col in range(0,x,WIDTH):
      new_square = []
      for i in range(row, row+WIDTH):
        new_square.append(sql[i][col:col+WIDTH])
      new_row.append("/".join(new_square))
    rows.append(new_row)
  return rows

def stitch(rows):
  to_stitch = []
  x,y = shape(rows[0][0])
  for row in rows: 
    rowm = map(lambda x: x.split("/"), row)
    for i in range(x):
      new_row = ""
      for j in range(len(row)):
        new_row += rowm[j][i]
      to_stitch.append(new_row)
  return "/".join(to_stitch)

def transform(sqs, rules):
  for row in range(len(sqs)):
    for col in range(len(sqs[0])):
      m = search(sqs[row][col], rules)
      if len(m) > 1: print "More than one match."
      rule = m.pop()
      sqs[row][col] = rules[rule]
  return sqs
    
def search(sq, rules):
  matches = set()

  ## search unflipped space
  if sq in rules:
    matches.add(sq)
  r = sq
  for _ in range(3):
    r = rotate(r)
    if r in rules:
      matches.add(r)
    
  ## search flipped space
  flipped = flip(sq)  

  if flipped in rules:
    matches.add(flipped)
  rf = flipped
  for _ in range(3):
    rf = rotate(rf)
    if rf in rules:
      matches.add(rf)
  return matches

def square_print(sq):
  print ''
  for row in sq.split("/"):
    print row

def shape(sq):
  s = sq.split("/")
  return (len(s), len(s[1])) 

def flip(sq):
  rows = sq.split("/")

  if len(rows[0]) > 3:
    print "Unexpected square size {}. No flip."
    return sq

  res = []
  for row in rows:
    x = list(row)
    x[0],x[-1] = x[-1], x[0]
    res.append(''.join(x))

  return '/'.join(res)

def rotate(sq):
  rows = sq.split("/")
  if len(rows[0]) == 3:
     
    r1 = sq[8] + sq[4] + sq[0]
    r2 = sq[9] + sq[5] + sq[1]
    r3 = sq[10] + sq[6] + sq[2]

    return r1 + "/" + r2 + "/" + r3 
  else:
    r1 = sq[3] + sq[0]
    r2 = sq[4] + sq[1]
    return r1 + "/" + r2

def amatch(sq1, sq2):
  return sq1 == sq2

def load_rules(fname):
  rules = {}
  with open(fname, 'r') as f:
    for rule in f.readlines():
      key, val = rule.strip().split("=>")
      rules[key.strip()] = val.strip()
  return rules

def go(start, rules, num=1):
  for _ in range(num):
    d = divide(start)
    t = transform(d, rules)
    start = stitch(t)
  return start

def count_on(sq):
  return sum(map(lambda x: 1 if x=="#" else 0, list(sq)))
  

if __name__ == "__main__":
  FILENAME = 'rules'

  start = '.#./..#/###'
  rules = load_rules(FILENAME)
  res = go(start, rules, num=5)

  print "part I:"
  print "  on after five steps:", count_on(res)

  start = '.#./..#/###'
  res = go(start, rules, num=18)

  print "\npart II:"
  print "  on after five steps:", count_on(res)



    

