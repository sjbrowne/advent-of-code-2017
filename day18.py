
from collections import defaultdict
import re

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
  return 1 if x <= 0 else y

def read_until_rcv(instrs):
  regs = defaultdict(int)

  i = 0
  while i >= 0 and i < len(instrs):
    jp = 1
    s = re.split(' ', instrs[i].strip()) 
    assm, vars = s[0], s[1:]

    if assm == "mul":
      x,y = vars[0], vars[1]
      mul(x,y,regs)

    if assm == "add":
      x,y = vars[0], vars[1]
      add(x,y,regs)

    if assm == "mod":
      x,y = vars[0], vars[1]
      mod(x,y,regs)

    if assm == "set":
      x,y = vars[0], vars[1]
      sek(x,y,regs)

    if assm == "jgz":
      x,y = vars[0], vars[1]
      if not not regs[x]:
        jp = jmp(x,y,regs) 

    if assm == "rcv":
      x = vars[0]
      freq = rcv(x, regs)
      if freq != None:
        return freq

    if assm == "snd":
      x = vars[0]
      snd(x, regs)
    i+=jp

def read_two_programs(instrs):
  LIMIT = len(instrs)

  regs0 = defaultdict(int)
  regs1 = defaultdict(int)
  regs0['p'], regs1['p'] = 0,1

  jmps = {}

  queue0 = []
  queue1 = []

  i0,i1 = 0,0

  c = 0
  send_count = 0

  program_one_running = i0 >= 0 and i0 < LIMIT 
  program_two_running = i1 >= 0 and i1 < LIMIT

  while program_one_running and program_two_running: #and c < 1000:
    c += 1
    jmps['0'], jmps['1'] = 1,1
    jp0, jp1 = 1,1
    s0 = re.split(' ', instrs[i0].strip()) 
    s1 = re.split(' ', instrs[i1].strip()) 
    assm0, vars0 = s0[0], s0[1:]
    assm1, vars1 = s1[0], s1[1:]

    ## ---- program 0 ------

    if assm0 == "mul":
      x,y = vars0[0], vars0[1]
      mul(x,y,regs0)

    if assm0 == "add":
      x,y = vars0[0], vars0[1]
      add(x,y,regs0)

    if assm0 == "mod":
      x,y = vars0[0], vars0[1]
      mod(x,y,regs0)

    if assm0 == "set":
      x,y = vars0[0], vars0[1]
      sek(x,y,regs0)

    if assm0 == "jgz":
      x,y = vars0[0], vars0[1]
      #jmps['0'] = jmp(x,y,regs0) 
      jp0 = jmp(x,y,regs0) 

    if assm0 == "rcv":
      if len(queue0) == 0:
        jp0 = 0 
      else:
        x = vars0[0]
        r0 = queue0.pop(0)
        regs0[x] = r0

    if assm0 == "snd":
      x = vars0[0]
      x = int(x) if x.isdigit() or x[0] == '-' else regs0[x]
      queue1.append(x)


    ## ---- program 1 ------

    if assm1 == "mul":
      x,y = vars1[0], vars1[1]
      mul(x,y,regs1)

    if assm1 == "add":
      x,y = vars1[0], vars1[1]
      add(x,y,regs1)

    if assm1 == "mod":
      x,y = vars1[0], vars1[1]
      mod(x,y,regs1)

    if assm1 == "set":
      x,y = vars1[0], vars1[1]
      sek(x,y,regs1)

    if assm1 == "jgz":
      x,y = vars1[0], vars1[1]
      jp1 = jmp(x,y,regs1) 

    if assm1 == "rcv":
      if len(queue1) == 0:
        jp1 = 0
      else:
        x = vars1[0]
        r1 = queue1.pop(0)
        regs1[x] = r1
      
    if assm1 == "snd":
      send_count += 1
      x = vars1[0]
      x = int(x) if x.isdigit() or x[0] == '-' else regs1[x]
      queue0.append(x)

    i0+=jp0
    i1+=jp1

    program_one_running = i0 >= 0 and i0 < LIMIT
    program_two_running = i1 >= 0 and i1 < LIMIT 

    if jp0 == 0 and jp1 == 0:
      break
  return send_count
      

if __name__ == "__main__":

  with open('duetasm', 'r') as f:
    I = map(lambda x: x.strip(), f.readlines())

  freq = read_until_rcv(I)

  print "part I:"
  print "  freq at recover: ", freq

  s = read_two_programs(I)
  print "\npart II:"
  print "  send count:      ", s
