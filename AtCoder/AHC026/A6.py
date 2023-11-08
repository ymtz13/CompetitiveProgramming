from random import randint, seed, random
from math import exp


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


def solve(ss=0):
    seed(ss)

    def randintwo(s, t, w):
        x = randint(s, t - 1)
        if x == w:
            x = t
        return x

    s0 = State(N, M, B)
    states = [s0.clone() for _ in range(T)]

    temp = 10
    for v in range(1, N + 1):
        # r = 0.98
        # r = 0.2 + ((N - v) / N) * 0.8
        # R = int(T * r)
        temp *= 0.996

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

                if len(heads) >= 6 and randint(1, 100) <= 30:
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

        mincost = min(s.cost for s in states)
        states = [s for s in states if exp(-(s.cost - mincost) / temp) > random()]
        states.sort(key=lambda s: s.cost)

        states.extend(states[i % len(states)].clone() for i in range(T - len(states)))

    best = states[0]
    for s in states:
        if s.cost < best.cost:
            best = s

    return best, states


best, states = solve(ss=0)

for v, idest in best.history:
    # print(v, idest)
    pass

# print(best.cost, {s.cost for s in states})


total = 0
for ss in range(10):
    best, states = solve(ss)
    print(best.cost, {s.cost for s in states})
    total += best.cost

print(total)
