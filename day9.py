def score(S):
  i,o,s,g = 0,0,0,0
  ingarb = False
  while i < len(S):
    if ingarb:
      if S[i] == '>':
        ingarb = False
        i += 1
      elif S[i] == '!':
        i += 2
      else:
        i += 1
        g += 1
    else:
      if S[i] == '}':
        s+=o
        o-=1
      elif S[i] == '{':
        o+=1
      elif S[i] == '<':
        ingarb = True
      i+=1
  return (s,g)
    


def score2(S,d):
  print '\nS',S
  i = 0
  o = 0 
  s = 0
  g = 0 
  buf = ""
  while i < len(S):
    if S[i] == '{' and g == 0:                    ## open brace
      if o == 0:
        o += 1
        s += d+1
        i += 1
      else:
        j = i
        while o != 0:
          buf += S[j]
          if S[j] == '}':
            o -= 1
          elif S[j] == '{':
            o += 1
          j += 1
        s += score2(buf[:-1], d+1) 
        i = j
        print i
        print 'buffer', buf
        buf = ""
    elif S[i] == '}' and g == 0:                  ## close brace
      o -= 1
      buf = ""
      i += 1
    elif g == 0 and S[i] != "<":                  ## non-garbage non-brace
      if o > 0:
        buf += S[i]
      i+=1
    else:                                         ## garbage or ignore
      if S[i] == "!":
        i+=2
      elif S[i] == "<":
        g = 1
        i+=1
      elif S[i] == ">":
        g -= 1
        i+=1
      else:
        i+=1
  return s
        
        
        
if __name__ == "__main__":
  with open('stream', 'r') as f:
    for line in f.readlines():
      print score(line.strip())

  ### no garbage
  #print score("{}",0)
  #print score("{{}}",0)   
  #print score("{{{}}}",0)
  #print score("{}{}",0)
  #print score("{{},{}}",0)

  ### garbage
  #print '\ngarbage'
  #print score("{<a>,<a>,<a>,<a>}")
  #print score("{{<ab>},{<ab>},{<ab>},{<ab>}}")
  #print score("{{<!!>},{<!!>},{<!!>},{<!!>}}")
  #print score("{{<a!>},{<a!>},{<a!>},{<ab>}}")

  ### breaking recursive version
  #t1 = "{{{{{},{}},{{<o!!!!!>!>},<>,{<a>}},{<!>},<}!>!>,<<,\'u<,\"a!!uu!>,<>,{}},{{<!e\"!!!>}\",,!!,u!>},<!!!>o>}"
  #t2 = "{{<{!!<,a\'\'>,<!!!>u!>eeu,e!>,<o<>}},{<!>,<,,\"i!>,<!>,<!!!>o!a!!!!!>\'!>},<!!!>!!!>}"
  #t1_1 = "{{{},{}},{{<o!!!!!>!>},<>,{<a>}},{<!>},<}!>!>,<<,\'u<,\"a!!uu!>,<>,{}"
  #t1_2 = "{{},{}},{{<o!!!!!>!>},<>,{<a>}},{<!>},<"
  #t1_3 = "{<o!!!!!>!>},<>,{<a>}"
  #print score2(t1+t2,0)

