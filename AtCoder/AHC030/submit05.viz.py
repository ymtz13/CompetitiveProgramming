from classes import KnownIsland, Estimator, OilField, OilFieldShape, Vec
from math import floor

island = KnownIsland.from_stdin()
size = island.size

estimator = Estimator(island)

for _ in range(island.size_sq + 5):
    prob, possible_pos_list = estimator.estimate()
    pos = estimator.pick()

    if max(map(len, possible_pos_list)) == 1 or pos is None:
        ans = [Vec(ij // size, ij % size) for ij, p in enumerate(prob) if p > 1e-10]
        submit_response = island.submit_answer(ans)
        break

    pmax = max(prob)
    for i, p in enumerate(prob):
        v = floor(p / pmax * 255)
        c = f"{v:02x}"
        print(f"#c {i//size} {i%size} #{c}{c}{c}")

    result = island.query(pos)
    estimator.setQueryResult(pos, result)


if submit_response == 0:
    ans = []
    for i in range(island.size_sq):
        pos = Vec(i // size, i % size)
        if estimator.map[i] == 99:
            result = island.query(pos)
            estimator.setQueryResult(pos, result)

        if estimator.map[i]:
            ans.extend((pos.i, pos.j))

    print(f"a {len(ans)//2}", *ans)
