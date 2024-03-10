from classes import KnownIsland, Vec

island = KnownIsland.from_stdin()
size = island.size

oilcells = []

for i in range(size):
    for j in range(size):
        if (i + j) % 2:
            continue
        result = island.query(Vec(i, j))
        print(f"q 1 {i} {j}")
        if result > 0:
            oilcells.append((i, j))

neighbors = set()
for i, j in oilcells:
    if i + 1 < size:
        neighbors.add((i + 1, j))
    if 0 <= i - 1:
        neighbors.add((i - 1, j))
    if j + 1 < size:
        neighbors.add((i, j + 1))
    if 0 <= j - 1:
        neighbors.add((i, j - 1))

for i, j in neighbors:
    result = island.query(Vec(i, j))
    print(f"q 1 {i} {j}")
    if result > 0:
        oilcells.append((i, j))


num_oilcell = len(oilcells)
ans = []
for cell in oilcells:
    ans.extend(cell)
print(f"a {num_oilcell}", *ans)
