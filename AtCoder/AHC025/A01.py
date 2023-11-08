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
for _ in range(inp.Q):
    query = Query([0], [1])
    result = game.query(query)
assign = Assign([i % inp.D for i in range(inp.N)])
game.out(assign)
