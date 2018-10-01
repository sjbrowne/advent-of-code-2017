
def get_position(time, range):
  total = range*2 - 1
  return time % (total - 1)


def parse_layer(layer):
  layer = layer.strip().replace(" ", "")
  d,r = layer.split(":")
  return (int(d), int(r)) 
  

def collisions(layers):
  res = 0
  for layer in layers:
    d,r = parse_layer(layer) 
    pos = get_position(d, r) 
    if pos  == 0:
      res += d*r
  return res


def dont_get_caught(layers):
  parsed_layers = map(parse_layer, layers) 
  delay = 0 
  caught = True
  while caught:
    caught = False
    for layer in parsed_layers:
      d,r = layer
      pos = get_position(d+delay, r) 
      if pos == 0:
        caught = True
        break 
    delay += 1
  return delay-1



if __name__ == "__main__":

  with open('firewall', 'r') as f:
    layers = f.readlines()
  #layers = [
  #  "0: 3",
  #  "1: 2",
  #  "4: 4",
  #  "6: 4"
  #]

  print "part I:"
  print "  caught sum: ", collisions(layers)

  ## 3964778
  print "part II:"
  print "  delay:      ", dont_get_caught(layers)

