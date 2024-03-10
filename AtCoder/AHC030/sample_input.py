from random import randint, seed, choice
from classes import Vec, OilFieldShape

seed(100)

size = randint(10, 20)
size_sq = size * size


def is_valid_cell(cell: Vec):
    return 0 <= cell.i < size and 0 <= cell.j < size


def adjacents(cell):
    i, j = cell
    return filter(
        is_valid_cell, [Vec(i + 1, j), Vec(i - 1, j), Vec(i, j + 1), Vec(i, j - 1)]
    )


num_oilfield = randint(2, size_sq // 20)
epsilon = 0.01 * randint(1, 20)

oilfields = []

for _ in range(num_oilfield):
    a = randint(size_sq // 5, size_sq // 2) // num_oilfield
    d = randint(0, a - 4)

    s = randint(a - d, a + d)

    adj = {Vec(size // 2, size // 2)}
    cells = set()
    for _ in range(s):
        cell = choice(tuple(adj))
        cells.add(cell)
        adj.remove(cell)

        for cell_adj in adjacents(cell):
            if cell_adj not in cells:
                adj.add(cell_adj)

    oilfields.append(OilFieldShape(cells))


for of in oilfields:
    print(of)
