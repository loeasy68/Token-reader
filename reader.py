import sys
iota_counter = 0
def iota(reset=False):
  global iota_counter
  if reset:
    iota_counter += 1
  result = iota_counter
  iota_counter += 1
  return result

OP_PUSH=iota(True)
OP_PLUS=iota()
OP_EQUAL=iota()
OP_DUMP=iota()
COUNT_OPS=iota()
