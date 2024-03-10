from collections import deque
from itertools import permutations
from random import randint
from collections import defaultdict


def solve(K, A):
    A.sort()

    C = defaultdict(int)
    for a in A:
        C[a] += 1

    AA = A + [a + K for a in A]

    p = None
    B = []
    A = []
    for a in reversed(AA):
        if a != p:
            A.append(a)
            p = a
            B.append(0)
        B[-1] += 1

    # print(A)
    # print(B)

    pair = []
    queue = deque()
    for a, b in zip(A, B):
        for _ in range(b):
            if not queue or C[a % K] == 0:
                break
            v = queue.pop()
            pair.append(((v, a), (v % K, a % K), (a - v) % K))
            C[a % K] -= 1

        if a >= K:
            queue.extend([a] * b)

    print(pair)

    X = [x for _, _, x in pair]
    X.sort()
    ans = sum(X[1:])

    return ans


def naive(K, A):
    r = 0
    for p in permutations(A):
        v = 0
        for s, t in zip(p, p[1:]):
            v += (s - t) % K
        r = max(r, v)
    return r


N, K = map(int, input().split())
# A = list(map(int, input().split()))
A = [randint(0, K - 1) for _ in range(N)]

print(A)

ans = solve(K, A)
ans_naive = naive(K, A)
print(ans, ans_naive)

# print(pair)
print(ans)
