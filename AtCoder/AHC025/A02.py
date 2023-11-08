from random import randint, choice, seed

seed(100)


class Input:
    def __init__(self, N, D, Q):
        self.N = N
        self.D = D
        self.Q = Q

    def __str__(self):
        return f"Input {{ N: {self.N}, D: {self.D}, Q: {self.Q} }}"


class Query:
    def __init__(self, L, R):
        self.L = L
        self.R = R

    def __str__(self):
        return f"{len(self.L)} {len(self.R)} {' '.join(map(str, self.L))} {' '.join(map(str, self.R))}"


class Result:
    LT = -1
    GT = +1
    EQ = 0

    def __init__(self, query: Query, E):
        self.query = query
        self.E = E


class Assign:
    def __init__(self, assign):
        self.assign = assign

    def __str__(self):
        return " ".join(map(str, self.assign))


class Game:
    def init(self):
        N, D, Q = map(int, input().split())
        return Input(N, D, Q)

    def query(self, query: Query):
        print(query)
        res = input()

        if res == "<":
            E = Result.LT
        if res == ">":
            E = Result.GT
        if res == "=":
            E = Result.EQ

        return Result(query, E)

    def out(self, assign: Assign):
        print(assign)


game = Game()

inp = game.init()

D = [i % inp.D for i in range(inp.N)]
S = [set() for _ in range(inp.D)]
for i, d in enumerate(D):
    S[d].add(i)

for _ in range(inp.Q):
    dl = randint(0, inp.D - 1)
    dr = (dl + randint(1, inp.D - 1)) % inp.D
    sl = S[dl]
    sr = S[dr]
    listL = list(sl)
    listR = list(sr)

    query = Query(listL, listR)
    result = game.query(query)

    if result.E == result.EQ:
        continue

    if result.E == Result.LT:
        v = choice(listR)
        D[v] = dl
        sl.add(v)
        sr.remove(v)

        if len(sr) == 0:
            v = choice(listL)
            D[v] = dr
            sr.add(v)
            sl.remove(v)

    else:
        v = choice(listL)
        D[v] = dr
        sr.add(v)
        sl.remove(v)

        if len(sl) == 0:
            v = choice(listR)
            D[v] = dl
            sl.add(v)
            sr.remove(v)


assign = Assign(D)
game.out(assign)
