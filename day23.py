
from collections import defaultdict
import re

def is_prime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

def snd(x,    regs):
  regs['rcv'] = regs[x]

def rcv(x,    regs):
  return regs['rcv'] if not not regs[x] else None

def sek(x, y, regs):
  if y.isdigit() or y[0] == '-':
    regs[x] = int(y)
  else:
    regs[x] = regs[y]

def add(x, y, regs):
  if y.isdigit() or y[0] == '-':
    regs[x] += int(y)
  else:
    regs[x] += regs[y]

def sub(x, y, regs):
  if y.isdigit() or y[0] == '-':
    regs[x] -= int(y)
  else:
    regs[x] -= regs[y]

def mul(x, y, regs):
  if y.isdigit() or y[0] == '-':
    regs[x] *= int(y)
  else:
    regs[x] *= regs[y]

def mod(x, y, regs):
  if y.isdigit() or y[0] == '-':
    regs[x] %= int(y)
  else:
    regs[x] %= regs[y]

def jmp(x, y, regs):
  y = int(y) if y.isdigit() or y[0] == '-' else regs[y]
  x = int(x) if x.isdigit() or x[0] == '-' else regs[x]
  return 1 if x == 0 else y

def form_regs(regs):
  s = ""
  for x in regs:
    s += x+":"+str(regs[x])+" "
  return s

def count_mults(instrs):
  regs = defaultdict(int)

  i = 0
  cmult = 0
  while i >= 0 and i < len(instrs):
    jp = 1
    s = re.split(' ', instrs[i].strip()) 
    assm, vars = s[0], s[1:]

    if assm == "mul":
      x,y = vars[0], vars[1]
      mul(x,y,regs)
      cmult += 1

    if assm == "add":
      x,y = vars[0], vars[1]
      add(x,y,regs)

    if assm == "sub":
      x,y = vars[0], vars[1]
      sub(x,y,regs)

    if assm == "mod":
      x,y = vars[0], vars[1]
      mod(x,y,regs)

    if assm == "set":
      x,y = vars[0], vars[1]
      sek(x,y,regs)

    if assm == "jnz":
      x,y = vars[0], vars[1]
      jp = jmp(x,y,regs) 

    i+=jp
  return cmult

def get_reg_h(instrs):
  regs = defaultdict(int)
  i = 0
  regs['a'] = 1
  while regs['f'] == 0:
    jp = 1
    s = re.split(' ', instrs[i].strip()) 
    assm, vars = s[0], s[1:]

    if assm == "mul":
      x,y = vars[0], vars[1]
      mul(x,y,regs)

    if assm == "add":
      x,y = vars[0], vars[1]
      add(x,y,regs)

    if assm == "sub":
      x,y = vars[0], vars[1]
      sub(x,y,regs)

    if assm == "mod":
      x,y = vars[0], vars[1]
      mod(x,y,regs)

    if assm == "set":
      x,y = vars[0], vars[1]
      sek(x,y,regs)

    if assm == "jnz":
      x,y = vars[0], vars[1]
      jp = jmp(x,y,regs) 

    i+=jp

  hset = 0
  for i in range(regs['b'], regs['c']+1, 17):
    if not is_prime(i):
      hset += 1

  return hset
      

if __name__ == "__main__":

  with open('fireasm', 'r') as f:
    I = map(lambda x: x.strip(), f.readlines())

  mults = count_mults(I)

  print "part I:"
  print "  mults executed: ", mults

  h = get_reg_h(I)

  print "\npart II:"
  print "  h sets: ", h

