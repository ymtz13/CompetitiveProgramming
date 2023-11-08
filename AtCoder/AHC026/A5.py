from random import randint, seed

seed(0)


def randintwo(s, t, w):
    x = randint(s, t - 1)
    if x == w:
        x = t
    return x


class State:
    def __init__(self, N, M, B, history=[], cost=0):
        self.N = N
        self.M = M
        self.B = B

        self.HeightOf = [len(b) for b in B]
        self.PileOf = [None] * (N + 1)
        self.LocaOf = [None] * (N + 1)

        for i, b in enumerate(B):
            for j, v in enumerate(b):
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

        piece = B[i][j:]
        del B[i][j:]
        B[idest].extend(piece)

        for k, vv in enumerate(piece):
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

        del B[i][-1]
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
B = [[]] + [list(map(int, input().split())) for _ in range(M)]

T = 1000
r = 0.9
R = int(T * r)

s0 = State(N, M, B)
states = [s0.clone() for _ in range(T)]

for v in range(1, N + 1):
    for s in states:
        heads = s.heads(v)
        if heads:
            i = s.PileOf[v]

            # idest = (i % M) + 1
            # s.move(heads[0], idest)

            # idest = randint(1, s.M - 1)
            # if idest == i:
            #     idest = s.M
            # s.move(heads[0], idest)

            if len(heads) >= 4 and randint(1, 100) <= 50:
                t = randint(1, len(heads) - 1)
                heads0 = heads[:t]
                heads1 = heads[t:]
                idest0 = randintwo(1, s.M, i)
                idest1 = randintwo(1, s.M, i)
                s.move(heads1[0], idest1)
                s.move(heads0[0], idest0)
            else:
                idest = randintwo(1, s.M, i)
                s.move(heads[0], idest)

        s.pick(v)

    states.sort(key=lambda s: s.cost)
    states = states[:R] + [s.clone() for s in states[: T - R]]

best = states[0]
for s in states:
    if s.cost < best.cost:
        best = s

for v, idest in best.history:
    print(v, idest)

print(best.cost, {s.cost for s in states})
