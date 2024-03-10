N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solve(Q, A, B):
    m = 0
    for ma in range(max(Q) + 1):
        v = 1 << 60
        for a, b, q in zip(A, B, Q):
            r = q - a * ma
            if r < 0:
                return m

            if b == 0:
                continue

            v = min(v, r // b)

        m = max(m, ma + v)

    return m


print(solve(Q, A, B))
