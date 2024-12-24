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
    
def get_wire_value(wire_start_with):
    subwires = []
    for wire in wires:
        if wire.startswith(wire_start_with):
            subwires.append((int(wire[1:]), wires[wire]))
    subwires.sort(reverse=True)
    return ''.join([str(int(wire[1])) for wire in subwires])

x = get_wire_value('x')
y = get_wire_value('y')
print('x:', x)
print('y:', y)
z = int(x, 2) + int(y, 2)
print('z:', z)
print('z in binary:', bin(z))
print('z as part 1: 0b1100110010111101011100001101110011111100100110')

with open('x.dot', 'w') as f:
    f.write('digraph {\n')
    f.write('node [fontname="Consolas", shape=box width=.5];\n')
    f.write('splines=ortho;\nrankdir="LR";\n')

    opid = 1
    opnames = {'XOR': '^', 'AND': '&', 'OR': '|'}
    opcolors = {'XOR': 'darkgreen', 'AND': 'red', 'OR': 'blue'}
    for line in lines[i+1:]:
        line = line.split(' -> ')
        output = line[1]
        operation = line[0].split(' ')
        a = operation[0]
        op = operation[1]
        b = operation[2]
        if output.startswith('z'):
            f.write(f'{output} [color="purple" fontcolor="purple"];\n')

        f.write(f'op{opid} [label="{opnames[op]}" color="{opcolors[op]}"'
                f'fontcolor="{opcolors[op]}"];\n')
        f.write(f'{a} -> op{opid};\n')
        f.write(f'{b} -> op{opid};\n')
        f.write(f'op{opid} -> {output};\n')
        opid += 1

    f.write('}\n')

# Swaps seen in graph
swaps = [
  'dhg', 'z06',
  'dpd', 'brk',
  'bhd', 'z23',
  'nbf', 'z38',
]

swaps.sort()
print(','.join(swaps))