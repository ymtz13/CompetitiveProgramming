x1, y1, x2, y2 = map(int, input().split())

D = [
    (+1, +2),
    (+1, -2),
    (-1, +2),
    (-1, -2),
    (+2, -1),
    (+2, +1),
    (-2, -1),
    (-2, +1),
]

P1 = {(x1 + dx, y1 + dy) for dx, dy in D}
P2 = {(x2 + dx, y2 + dy) for dx, dy in D}

print('Yes' if P1 & P2 else 'No')
