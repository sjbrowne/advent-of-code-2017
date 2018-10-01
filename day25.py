from collections import defaultdict

def turing_machine(start, limit):
  n,c = 0,0  
  tape = defaultdict(int)
  state = start
  while c < limit:
    if state == 'A': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "B"
        n+=1
      else:  
        tape[n] = 0
        state = "C"
        n-=1
    elif state == 'B': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "A"
        n-=1
      else:  
        tape[n] = 1
        state = "D"
        n+=1
    elif state == 'C': 
      if tape[n] == 0:  
        tape[n] = 0
        state = "B"
        n-=1
      else:  
        tape[n] = 0
        state = "E"
        n-=1
    elif state == 'D': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "A"
        n+=1
      else:  
        tape[n] = 0
        state = "B"
        n+=1
    elif state == 'E': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "F"
        n-=1
      else:  
        tape[n] = 1
        state = "C"
        n-=1
    elif state == 'F': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "D"
        n+=1
      else:  
        tape[n] = 1
        state = "A"
        n+=1
    c+=1
  return tape

def turing_machine_test(start, limit):
  n,c = 0,0  
  tape = defaultdict(int)
  state = start
  while c < limit:
    print 'n:', n
    if state == 'A': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "B"
        n+=1
      else:  
        tape[n] = 0
        state = "B"
        n-=1
    elif state == 'B': 
      if tape[n] == 0:  
        tape[n] = 1
        state = "A"
        n-=1
      else:  
        tape[n] = 1
        state = "A"
        n+=1
    c+=1
  return tape


if __name__ == "__main__":

  STEPS = 12667664
  tape = turing_machine("A", STEPS)

  ones = 0
  for x in tape: ones += tape[x]

  print "part I:"
  print "  checksum: ", ones


