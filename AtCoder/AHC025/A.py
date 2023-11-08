from random import randint, choice, shuffle, choices, seed
from math import exp
from itertools import accumulate
import matplotlib.pyplot as plt
from collections import defaultdict

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


class TestGame:
    N = 30  # [30, 100]
    N = 30  # [30, 100]
    D = 5  # [2, N/4]
    Q = 8 * N

    W = [
        820,
        2574,
        3143,
        11789,
        12187,
        15760,
        18107,
        27072,
        38517,
        42749,
        44462,
        48230,
        54965,
        59056,
        67101,
        72591,
        77770,
        78056,
        87306,
        100604,
        115470,
        127025,
        133858,
        143254,
        143633,
        151665,
        217461,
        228747,
        244944,
        350543,
    ]

    def init(self):
        # self.W = shuffle(self.W)
        return Input(TestGame.N, TestGame.D, TestGame.Q)

    def query(self, query: Query):
        sl = sum([TestGame.W[i] for i in query.L])
        sr = sum([TestGame.W[i] for i in query.R])

        if sl < sr:
            E = Result.LT
        if sl > sr:
            E = Result.GT
        if sl == sr:
            E = Result.EQ

        print(
            "query:",
            query.L,
            query.R,
            sl,
            "<" if E == Result.LT else ">" if E == Result.GT else "=",
            sr,
        )

        return Result(query, E)

    def out(self, assign: Assign):
        print(assign)


LAMBDA = 1e-5

# game = Game()
game = TestGame()
inp = game.init()


class Distribution:
    PARTITION = 1000
    MAX = 100000 * inp.N // inp.D
    STEP = MAX / PARTITION

    def __init__(self, value):
        self.value = value
        s = sum(value)
        self.normalized_value = [v / s for v in value]

        self.mean = sum(x * p for x, p in zip(Distribution.X, self.normalized_value))
        self.mean2 = self.mean * self.mean
        self.var = (
            sum(xx * p for xx, p in zip(Distribution.X2, self.normalized_value))
            - self.mean2
        )

        self.left_value = None
        self.right_value = None

    def left(self):
        if not self.left_value:
            left_value = [0] * Distribution.PARTITION
            s = 0
            for i, v in enumerate(reversed(self.normalized_value), 1):
                s += v
                left_value[-i] = s - v / 2

            self.left_value = Distribution(left_value)

        return self.left_value

    def right(self):
        if not self.right_value:
            right_value = [0] * Distribution.PARTITION
            s = 0
            for i, v in enumerate(self.normalized_value):
                s += v
                right_value[i] = s - v / 2

            self.right_value = Distribution(right_value)

        return self.right_value

    def mult(self, dist):
        value = [
            vl * vr for vl, vr in zip(self.normalized_value, dist.normalized_value)
        ]
        return Distribution(value)

    def offset(self, r=1):
        # m = min(self.normalized_value)
        value = [v + r / Distribution.PARTITION for v in self.normalized_value]
        return Distribution(value)

    def mean_dist(dists):
        value = dists[0].normalized_value
        for n, dist in enumerate(dists[1:], 2):
            value_next = [0] * Distribution.PARTITION

            cj = 1 / n
            ci = 1 - cj

            for i, vi in enumerate(value):
                for j, vj in enumerate(dist.normalized_value):
                    k = i * ci + j * cj
                    k0 = int(k)
                    k1 = k0 + 1

                    v = vi * vj

                    r0 = k1 - k
                    r1 = 1 - r0

                    value_next[k0] += v * r0
                    if k1 < Distribution.PARTITION:
                        value_next[k1] += v * r1

            value = value_next
        return Distribution(value)


Distribution.X = [Distribution.STEP * (n + 0.5) for n in range(Distribution.PARTITION)]
Distribution.X2 = [x * x for x in Distribution.X]
Distribution.INITIAL = [LAMBDA * exp(-LAMBDA * x) for x in Distribution.X]

"""dist = Distribution(value=Distribution.INITIAL)

dist2 = Distribution.mean_dist([dist, dist])
dist3 = Distribution.mean_dist([dist, dist, dist])
dist4 = Distribution.mean_dist([dist, dist, dist, dist])
dist5 = Distribution.mean_dist([dist, dist, dist, dist, dist])

print(1, dist.mean, dist.var)
print(2, dist2.mean, dist2.var)
print(3, dist3.mean, dist3.var)
print(4, dist4.mean, dist4.var)
print(5, dist5.mean, dist5.var)

dist4L = dist4.left()
dist4R = dist4.right()

plt.plot(Distribution.X, dist.normalized_value, linewidth=1, marker="o", markersize=2)
# plt.plot(Distribution.X, dist2.normalized_value, linewidth=1, marker="o", markersize=2)
# plt.plot(Distribution.X, dist3.normalized_value, linewidth=1, marker="o", markersize=2)
plt.plot(Distribution.X, dist4.normalized_value, linewidth=1, marker="o", markersize=2)
# plt.plot(Distribution.X, dist5.normalized_value, linewidth=1, marker="o", markersize=2)
plt.plot(Distribution.X, dist4L.normalized_value, linewidth=1, marker="o", markersize=2)
plt.plot(
    Distribution.X,
    dist4R.normalized_value,
    linewidth=1,
    marker="o",
    markersize=2,
)
plt.plot(
    Distribution.X,
    dist.mult(dist4R).normalized_value,
    linewidth=1,
    marker="o",
    markersize=2,
)
plt.grid(True)
plt.show()
"""

BATCH = 1

dists = [[i, Distribution(value=Distribution.INITIAL)] for i in range(inp.N)]


def plot(dists):
    for i, d in dists[:30]:
        plt.plot(
            Distribution.X,
            d.normalized_value,
            linewidth=1,
            marker="o",
            markersize=2,
            label=f"{i}({TestGame.W[i]})",
        )
    plt.legend()
    plt.grid(True)
    plt.show()


for _ in range(inp.Q):
    iL = randint(0, inp.N - 1)
    iR = (iL + randint(0, inp.N - 2)) % inp.N

    L = [dists[iL]]
    R = [dists[iR]]

    distL = Distribution.mean_dist([d for _, d in L])
    distR = Distribution.mean_dist([d for _, d in R])

    query = Query([i for i, _ in L], [i for i, _ in R])
    result = game.query(query)

    if result.E == Result.EQ:
        continue

    if result.E == Result.GT:
        L, R = R, L

    loff = distR.left()  # .offset(1)
    roff = distL.right()  # .offset(1)
    for tup in L:
        tup[1] = tup[1].mult(loff).offset(0.001)

    for tup in R:
        tup[1] = tup[1].mult(roff).offset(0.001)

plot(dists)

means = [dist.mean for _, dist in dists]

mean_all = sum(means) / inp.N
mean_group_size = inp.N / inp.D
mean_group_sum = mean_all * mean_group_size
mean_group_sum_sq = mean_group_sum**2

asg = [d % inp.D for d in range(inp.N)]


def sqsum(S):
    return sum([v * v for v in S])


S = [0] * inp.D
for mean, a in zip(means, asg):
    S[a] += mean


print(f"{sqsum(S):e} / {mean_group_sum_sq*inp.D:e}")
print(S, mean_group_sum)
print(sum(S), mean_group_sum * inp.D, sum(game.W))

for cnt in range(1000_000):
    rnd = randint(1, 5)

    temperature = 1000_000 - cnt

    if rnd >= 1:
        i = randint(0, inp.N - 1)
        m = means[i]

        f = asg[i]
        t = randint(0, inp.D - 1)

        sf0 = S[f]
        st0 = S[t]
        sf1 = sf0 - m
        st1 = st0 + m

        dE = sf1 * sf1 + st1 * st1 - sf0 * sf0 - sf1 * sf1

        if dE < 0:
            asg[i] = t
            S[f] = sf1
            S[t] = st1

    else:
        pass

print(f"{sqsum(S):e} / {mean_group_sum_sq*inp.D:e}")
print(S, mean_group_sum)


assign = Assign(asg)
game.out(assign)
