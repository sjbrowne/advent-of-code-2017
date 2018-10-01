from collections import defaultdict

REG = defaultdict(int)

def get_cond(I):
  I.split('if')

def check_cond(cond):
  pass

def parse(instr, REGS):
  action, cond = instr.strip().split("if") 
  var, op, oprnd = cond.strip().split(" ")
  conds = "REGS[\'{}\'] {} {}".format(var, op, oprnd)
  if eval(conds):
    key, mov, val = action.strip().split(" ")
    REGS[key] = REGS[key] + int(val) if mov == "inc" else REGS[key] - int(val)


if __name__ == "__main__":
  
  R = defaultdict(int)
  M = -1e9
  with open('reginstr', 'r') as f:
    for instr in f.readlines():
      parse(instr, R) 
      m = max(R.items(), key=lambda x: x[1])
      if m[1] > M: M = m[1]

  m = max(R.items(), key=lambda x: x[1])
  print 'high:    ', m[1]
  print 'highest: ', M
  


  
  
