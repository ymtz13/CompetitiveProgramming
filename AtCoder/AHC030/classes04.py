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

        self.exact_value = [0] * self.size_sq
        for ij in range(self.size_sq):
            pos = Vec(ij // size, ij % size)
            cnt = len([of for of in oilfields if of.contains(pos)])
            self.exact_value[ij] = cnt

        self.exact_answer = {
            Vec(ij // size, ij % size) for ij, ev in enumerate(self.exact_value) if ev
        }

    def query(self, pos: Vec):
        print(f"q 1 {pos.i} {pos.j}")
        return self.exact_value[pos.i * self.size + pos.j]

    def submit_answer(self, pos_list):
        ans = []
        for pos in pos_list:
            ans.extend(pos)
        print(f"a {len(pos_list)}", *ans)

        return 1 if self.exact_answer == set(pos_list) else 0

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

    def submit_answer(self, pos_list):
        ans = []
        for pos in pos_list:
            ans.extend(pos)
        print(f"a {len(pos_list)}", *ans)
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
        self.map = [99] * island.size_sq
        self.confirmed = [0] * island.size_sq
        self.confirmed_pos = [None] * len(island.oilfieldshapes)

    def estimate(self):
        island = self.island
        size = island.size
        size_sq = island.size_sq

        while True:
            prob = [0] * size_sq
            possible_pos_list = []
            redo = False

            for ishape, shape in enumerate(island.oilfieldshapes):
                box = shape.box
                cnt = [0] * island.size_sq
                possible_pos = []

                if self.confirmed_pos[ishape] is None:
                    for di in range(size - box.i + 1):
                        for dj in range(size - box.j + 1):
                            ok = True
                            for cell in shape.cells:
                                i = cell.i + di
                                j = cell.j + dj
                                ij = i * size + j
                                if self.map[ij] - self.confirmed[ij] == 0:
                                    ok = False
                                    break

                            if ok:
                                possible_pos.append(Vec(di, dj))

                    if len(possible_pos) == 1:
                        redo = True
                        self.confirmed_pos[ishape] = possible_pos[0]
                        print(f"# confirmed: {ishape}")
                        print(f"#c 0 0 red")
                        di, dj = possible_pos[0]
                        for cell in shape.cells:
                            i = cell.i + di
                            j = cell.j + dj
                            self.confirmed[i * island.size + j] += 1

                else:
                    possible_pos = [self.confirmed_pos[ishape]]

                possible_pos_list.append(possible_pos)

                for di, dj in possible_pos:
                    for cell in shape.cells:
                        i = cell.i + di
                        j = cell.j + dj
                        cnt[i * island.size + j] += 1

                prob_solo = [c / len(possible_pos) for c in cnt]
                prob = [1 - (1 - p) * (1 - ps) for p, ps in zip(prob, prob_solo)]

            if not redo:
                return prob, possible_pos_list

    def setQueryResult(self, pos: Vec, value: int):
        self.map[pos.i * self.island.size + pos.j] = value

    def pick(self):
        prob, _ = self.estimate()

        prob_indexed = [
            (p, i) for i, p in enumerate(prob) if p > 1e-10 and self.map[i] == 99
        ]
        prob_indexed.sort()

        if not prob_indexed:
            return None

        prev = None
        for p, ij in prob_indexed:
            if p > 0.5:
                break
            prev = (p, ij)

        if prev:
            ij = prev[1]

        return Vec(ij // self.island.size, ij % self.island.size)
