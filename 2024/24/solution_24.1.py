input = open('./input_24.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

wires = {}

n = len(lines)
i = 0
while lines[i] != '':
    line = lines[i].split(': ')
    wires[line[0]] = bool(int(line[1]))
    i += 1

def handle_line(line):
    line = line.split(' -> ')
    output = line[1]
    operation = line[0].split(' ')
    a = operation[0]
    op = operation[1]
    b = operation[2]
    if not a in wires or not b in wires:
        return False
    if op == 'AND':
      wires[output] = wires[a] & wires[b]
    if op == 'OR':
      wires[output] = wires[a] | wires[b]
    if op == 'XOR':
      wires[output] = wires[a] ^ wires[b]
    return True

waitstack = []
for line in lines[i+1:]:
    handled = False
    while not handled:
      handled = True
      for waitline in waitstack:
          if handle_line(waitline):
              waitstack.remove(waitline)
              handled = False
              break
    
    if not handle_line(line):
        waitstack.append(line)
    
while len(waitstack) > 0:
    for waitline in waitstack:
        if handle_line(waitline):
            waitstack.remove(waitline)
            break 

zwires = []
for wire in wires:
    if wire.startswith('z'):
        zwires.append((int(wire[1:]), wires[wire]))

zwires.sort(reverse=True)
zstring = ''.join([str(int(wire[1])) for wire in zwires])
print(zstring)
ans = int(zstring, 2)
print(ans)