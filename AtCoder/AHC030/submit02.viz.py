from classes import KnownIsland, Estimator
from math import floor

island = KnownIsland.from_stdin()
size = island.size

estimator = Estimator(island)

for _ in range(island.size_sq):
    prob, possible_pos_list = estimator.estimate()
    pos = estimator.pick()

    if max(map(len, possible_pos_list)) == 1 or pos is None:
        ans = []
        for i, p in enumerate(prob):
            if p > 1e-10:
                ans.extend((i // size, i % size))
        print(f"a {len(ans)//2}", *ans)
        exit()

    pmax = max(prob)
    for i, p in enumerate(prob):
        v = floor(p / pmax * 255)
        c = f"{v:02x}"
        print(f"#c {i//size} {i%size} #{c}{c}{c}")

    result = island.query(pos)
    estimator.setQueryResult(pos, result)
