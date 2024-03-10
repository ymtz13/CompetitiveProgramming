N = int(input())
A = list(map(int, input().split()))


def solve(A):
    minA = min(A)
    for i, a in enumerate(A):
        if a == minA:
            break

    A = A[i:] + A[:i]

    D = []
    for a, b in zip(A, A[1:] + [A[0]]):
        D.append(b - a)

    S = sum([d for d in D if d > 0])

    s = S
    m = S
    for d in reversed(D):
        s += d
        m = min(m, s)

    return S + max(0, minA - m)


print(solve(A))
exit()

S = {(0,) * 6}
V = [[(0,) * 6]]

for _ in range(7):
    v = V[-1]
    vnext = []

    for t in v:
        for i in range(6):
            for k in range(1, 7):
                z = list(t)
                for x in range(i, i + k):
                    z[x % 6] += 1
                z = tuple(z)
                if z not in S:
                    S.add(z)
                    vnext.append(z)

    V.append(vnext)
    # print(_, v)
    # input()

for n, v in enumerate(V):
    for a in v:
        s = solve(list(a))
        if n != s:
            print(a, n, s)
