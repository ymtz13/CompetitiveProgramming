from collections import namedtuple

Vec = namedtuple("Vec", ["i", "j"])


class OilFieldShape:
    def __init__(self, cells):
        ilist = [cell.i for cell in cells]
        jlist = [cell.j for cell in cells]

        imin = min(ilist)
        imax = max(ilist)
        jmin = min(jlist)
        jmax = max(jlist)

        cells = [Vec(i - imin, j - jmin) for i, j in cells]

        self.cells = cells
        self.size = len(cells)

        self.box = Vec(imax - imin + 1, jmax - jmin + 1)

    def from_tuple(tup):
        cells = [Vec(i, j) for i, j in zip(tup[1::2], tup[2::2])]
        return OilFieldShape(cells)

    def __str__(self):
        lines = [f"OilFieldShape [size:{self.size: 3d}]  [box:{self.box}]"]

        table = [["."] * self.box.j for _ in range(self.box.i)]
        for cell in self.cells:
            table[cell.i][cell.j] = "#"

        for row in table:
            lines.append("".join(row))

        return "\n".join(lines)


class OilField:
    def __init__(self, shape: OilFieldShape, pos: Vec):
        self.shape = shape
        self.pos = pos

    def contains(self, pos):
        relpos = Vec(pos.i - self.pos.i, pos.j - self.pos.j)
        return relpos in self.shape.cells


class KnownIsland:
    def __init__(self, size: int, oilfields):
        self.size = size
        self.size_sq = size * size
        self.oilfields = oilfields
        self.oilfieldshapes = [of.shape for of in oilfields]

    def query(self, pos: Vec):
        print(f"q 1 {pos.i} {pos.j}")
        cnt = 0
        for oilfield in self.oilfields:
            if oilfield.contains(pos):
                cnt += 1
        return cnt

    def from_stdin():
        size, num_oilfield, epsilon = input().split()
        size = int(size)
        num_oilfield = int(num_oilfield)
        epsilon = float(epsilon)

        ofshapetuples = [tuple(map(int, input().split())) for _ in range(num_oilfield)]
        ofshapes = [OilFieldShape.from_tuple(tup) for tup in ofshapetuples]

        ofposs = [Vec(*map(int, input().split())) for _ in range(num_oilfield)]

        oilfields = [OilField(shape, pos) for shape, pos in zip(ofshapes, ofposs)]

        return KnownIsland(size, oilfields)


class UnchartedIsland:
    def __init__(self, size: int, oilfieldshapes):
        self.size = size
        self.size_sq = size * size
        self.oilfieldshapes = oilfieldshapes

    def query(self, pos: Vec):
        print(f"q 1 {pos.i} {pos.j}")
        return int(input())

    def from_stdin():
        size, num_oilfield, epsilon = input().split()
        size = int(size)
        num_oilfield = int(num_oilfield)
        epsilon = float(epsilon)

        ofshapetuples = [tuple(map(int, input().split())) for _ in range(num_oilfield)]
        ofshapes = [OilFieldShape.from_tuple(tup) for tup in ofshapetuples]

        return UnchartedIsland(size, ofshapes)


class Game:
    def __init__(self, island):
        self.island = island


class Estimator:
    def __init__(self, island: UnchartedIsland):
        self.island = island
        self.map = [None] * island.size_sq

    def estimate(self):
        island = self.island
        size = island.size

        prob = [0] * island.size_sq
        possible_pos_list = []
        for shape in island.oilfieldshapes:
            box = shape.box
            cnt = [0] * island.size_sq
            possible_pos = []

            for di in range(size - box.i + 1):
                for dj in range(size - box.j + 1):
                    ok = True
                    for cell in shape.cells:
                        i = cell.i + di
                        j = cell.j + dj
                        if self.map[i * size + j] == 0:
                            ok = False
                            break

                    if ok:
                        possible_pos.append(Vec(di, dj))

            possible_pos_list.append(possible_pos)

            for di, dj in possible_pos:
                for cell in shape.cells:
                    i = cell.i + di
                    j = cell.j + dj
                    cnt[i * island.size + j] += 1

            prob = [p + c / len(possible_pos) for p, c in zip(prob, cnt)]

        return prob, possible_pos_list

    def setQueryResult(self, pos: Vec, value: int):
        self.map[pos.i * self.island.size + pos.j] = value

    def pick(self):
        prob, _ = self.estimate()

        prob_indexed = [
            (p, i) for i, p in enumerate(prob) if p > 1e-10 and self.map[i] is None
        ]
        prob_indexed.sort()

        if not prob_indexed:
            return None

        i = prob_indexed[len(prob_indexed) // 2][1]

        return Vec(i // self.island.size, i % self.island.size)
