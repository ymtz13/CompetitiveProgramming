from collections import namedtuple, defaultdict
from itertools import product

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
        self.cells = [Vec(pos.i + cell.i, pos.j + cell.j) for cell in shape.cells]

    def contains(self, pos):
        relpos = Vec(pos.i - self.pos.i, pos.j - self.pos.j)
        return relpos in self.shape.cells


class KnownIsland:
    def __init__(self, size: int, oilfields):
        self.size = size
        self.size_sq = size * size
        self.oilfields = oilfields
        self.oilfieldshapes = [of.shape for of in oilfields]
        self.total_amount = sum([shape.size for shape in self.oilfieldshapes])

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
        self.total_amount = sum([shape.size for shape in self.oilfieldshapes])

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
    VEILED = 99

    def __init__(self, island: UnchartedIsland):
        self.island = island
        self.map = [Estimator.VEILED] * island.size_sq
        self.total_unveiled = 0
        self.confirmed = [0] * island.size_sq
        self.confirmed_pos = [None] * len(island.oilfieldshapes)
        self.required_pos = [set() for _ in island.oilfieldshapes]
        self.available_confs = None

    def estimate(self):
        island = self.island
        size = island.size
        size_sq = island.size_sq

        while True:
            prob = [0] * size_sq
            possible_pos_list = []
            possible_oilfield_list = [set() for _ in range(size_sq)]
            redo = False

            for ishape, shape in enumerate(island.oilfieldshapes):
                box = shape.box
                cnt = [0] * island.size_sq
                possible_pos = []

                if self.confirmed_pos[ishape] is None:
                    for di in range(size - box.i + 1):
                        for dj in range(size - box.j + 1):
                            ok = True
                            cells = set()
                            veiled_cells = 0
                            for cell in shape.cells:
                                i = cell.i + di
                                j = cell.j + dj
                                ij = i * size + j
                                cells.add(ij)

                                # 確定済みのセルを含む配置は無効
                                if self.map[ij] - self.confirmed[ij] == 0:
                                    ok = False
                                    break

                                if self.map[ij] == Estimator.VEILED:
                                    veiled_cells += 1

                            # 必須のセルを含まない配置は無効
                            if self.required_pos[ishape].difference(cells):
                                ok = False

                            # 未調査のセルの埋蔵量をすべて1としたとき総量を超えるような配置は無効
                            if veiled_cells + self.total_unveiled > island.total_amount:
                                ok = False

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
                        ij = i * island.size + j
                        cnt[ij] += 1
                        possible_oilfield_list[ij].add(ishape)

                prob_solo = [c / len(possible_pos) for c in cnt]
                prob = [1 - (1 - p) * (1 - ps) for p, ps in zip(prob, prob_solo)]

            for ij in range(size_sq):
                possible_oilfields = possible_oilfield_list[ij]
                if len(possible_oilfields) == self.map[ij]:
                    # possible_oilfields の要素である oilfield は必ずセル ij を含む配置となる
                    for i_oilfield in possible_oilfields:
                        if ij not in self.required_pos[i_oilfield]:
                            self.required_pos[i_oilfield].add(ij)
                            redo = True

            if not redo:
                return prob, possible_pos_list

    def setQueryResult(self, pos: Vec, value: int):
        ij = pos.i * self.island.size + pos.j
        self.map[ij] = value
        self.total_unveiled += value

        if self.available_confs:
            self.available_confs = [
                conf for conf in self.available_confs if conf[ij] == value
            ]

    def pick(self):
        island = self.island
        size = island.size
        size_sq = island.size_sq

        prob, possible_pos_list = self.estimate()

        # 配置を全列挙済みでない場合
        if not self.available_confs:

            # 配置の総数の上限
            n_max_confs = 1
            for possible_pos in possible_pos_list:
                n_max_confs *= len(possible_pos)

            if n_max_confs <= 8192:
                available_confs = []
                for possible_pos_combination in product(*possible_pos_list):
                    conf = [0] * size_sq
                    for shape, pos in zip(
                        island.oilfieldshapes, possible_pos_combination
                    ):
                        of = OilField(shape, pos)
                        for cell in of.cells:
                            ij = cell.i * size + cell.j
                            conf[ij] += 1

                    ok = True
                    for m, c in zip(self.map, conf):
                        if m != Estimator.VEILED and m != c:
                            ok = False
                            break

                    if ok:
                        available_confs.append(conf)

                self.available_confs = available_confs

            else:
                prob_indexed = [
                    (p, i)
                    for i, p in enumerate(prob)
                    if p > 1e-10 and self.map[i] == Estimator.VEILED
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

                return Vec(ij // size, ij % size)

        if len(self.available_confs) == 1:
            return None

        min_expected_next_confs = 1 << 60
        min_ij = None
        determined = True
        for ij, m in enumerate(self.map):
            if m != Estimator.VEILED:
                continue

            amount_dict = defaultdict(int)
            for conf in self.available_confs:
                amount_dict[conf[ij]] += 1

            if len(amount_dict) == 1:
                continue

            determined = False

            expected_next_confs = 0
            for value in amount_dict.values():
                expected_next_confs += value * value

            if expected_next_confs < min_expected_next_confs:
                min_expected_next_confs = expected_next_confs
                min_ij = ij

        if determined:
            return None

        return Vec(min_ij // size, min_ij % size)
