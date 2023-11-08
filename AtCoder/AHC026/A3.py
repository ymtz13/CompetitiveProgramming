from random import randint, seed

seed(0)


class State:
    def __init__(self, N, M, B, history=[], cost=0):
        self.N = N
        self.M = M
        self.B = B

        self.HeightOf = [None] * (M + 1)
        self.PileOf = [None] * (N + 1)
        self.LocaOf = [None] * (N + 1)

        for i, b in enumerate(B):
            for j, v in enumerate(b):
                if v is not None:
                    self.HeightOf[i] = j + 1
                    self.PileOf[v] = i
                    self.LocaOf[v] = j

        self.history = history[:]
        self.cost = cost

    def clone(self):
        B = [b[:] for b in self.B]
        new = State(self.N, self.M, B, self.history, self.cost)
        return new

    def move(self, v, idest):
        B = self.B
        HeightOf = self.HeightOf
        PileOf = self.PileOf
        LocaOf = self.LocaOf

        i = PileOf[v]
        if i == idest:
            self.cost += 99999
            return 99999

        j = LocaOf[v]
        hdest = HeightOf[idest]

        n = HeightOf[i] - j
        for k in range(n):
            vv = B[i][j + k]
            B[i][j + k] = None
            B[idest][hdest + k] = vv
            PileOf[vv] = idest
            LocaOf[vv] = hdest + k
        HeightOf[i] = j
        HeightOf[idest] = hdest + n

        self.history.append((v, idest))
        self.cost += n + 1

        return n + 1

    def pick(self, v):
        B = self.B
        HeightOf = self.HeightOf
        PileOf = self.PileOf
        LocaOf = self.LocaOf

        i = PileOf[v]
        j = LocaOf[v]
        if HeightOf[i] - 1 != j:
            return False

        B[i][j] = None
        PileOf[v] = 0
        LocaOf[v] = 0
        HeightOf[i] -= 1

        self.history.append((v, 0))

    def heads(self, v):
        B = self.B
        HeightOf = self.HeightOf
        PileOf = self.PileOf
        LocaOf = self.LocaOf

        i = PileOf[v]
        j = LocaOf[v]
        h = HeightOf[i]

        return B[i][j + 1 : h]


N, M = map(int, input().split())
B = [[]] + [list(map(int, input().split())) + [None] * N for _ in range(M)]

s0 = State(N, M, B)
trials = []

for trial in range(100):
    s = s0.clone()
    trials.append(s)

    for v in range(1, N + 1):
        heads = s.heads(v)
        if heads:
            i = s.PileOf[v]
            # idest = (i % M) + 1
            idest = randint(1, s.M - 1)
            if idest == i:
                idest = s.M
            s.move(heads[0], idest)

        s.pick(v)

best = trials[0]
for s in trials:
    if s.cost < best.cost:
        best = s

# print(best.cost, {s.cost for s in trials})

for v, idest in best.history:
    print(v, idest)
