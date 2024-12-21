from functools import lru_cache
from itertools import permutations

input = open('./input_21.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

@lru_cache(maxsize=None)
def get_deltas(a, b):
    if a == b:
        return 0, 0

    if len(set(a+b).intersection("<>v^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"

    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3
    bx, by = keypad.index(b) % 3, keypad.index(b) // 3

    return bx-ax, by-ay


@lru_cache(maxsize=None)
def is_valid_path(a, b, path):
    if len(set(a+b).intersection("<>v^")) > 0:
        keypad = "X^A<v>"
    else:
        keypad = "789456123X0A"

    ax, ay = keypad.index(a) % 3, keypad.index(a) // 3

    deltas = {
        "<": (-1, 0),
        ">": (1, 0),
        "v": (0, 1),
        "^": (0, -1)
    }

    for p in path:
        dx, dy = deltas[p]
        ax += dx
        ay += dy

        if ax < 0 or ax >= 3 or ay < 0 or ay >= len(keypad) // 3:
            return False

        if keypad[ay*3+ax] == "X":
            return False
    return True

@lru_cache(maxsize=None)
def get_all_paths(a, b):
    dx, dy = get_deltas(a, b)

    cx = "<" if dx < 0 else ">"
    cy = "^" if dy < 0 else "v"

    nx = cx * abs(dx) + cy * abs(dy)
    possible = []
    for p in permutations(nx):
        if is_valid_path(a, b, p):
            possible.append("".join(p) + "A")

    return possible

@lru_cache(maxsize=None)
def get_min_cost(seq, depth):
    ret = 0
    seq = "A" + seq
    for a, b in zip(seq, seq[1:]):
        ps = get_all_paths(a, b)
        if depth == 0:
            ret += min(len(p) for p in ps)
        else:
            ret += min(get_min_cost(p, depth-1) for p in ps)
    return ret


ans = 0
for code in lines:
    ans += get_min_cost(code, 2) * int(code[:-1])
print(ans)