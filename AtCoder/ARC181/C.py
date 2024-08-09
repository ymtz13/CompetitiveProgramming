def solve(N, P, Q):
    A = [[2] * N for _ in range(N)]

    for i in range(N):
        if i % 2 == 0:
            x = i // 2 + 1
            d = 0
        else:
            x = N - i // 2
            d = 1

        ip = P[x - 1] - 1
        iq = Q[x - 1] - 1

        for j in range(N):
            if A[ip][j] == 2:
                A[ip][j] = d
            if A[j][iq] == 2:
                A[j][iq] = d

    return A


def check(A, P, Q):
    R = list(enumerate(A, 1))
    C = list(enumerate(zip(*A), 1))
    print(R)
    print(C)

    R.sort(key=lambda x: x[1])
    C.sort(key=lambda x: x[1])
    RT = list(enumerate(P, 1))
    QT = list(enumerate(Q, 1))
    RT.sort(key=lambda x: x[1])
    QT.sort(key=lambda x: x[1])

    print([v for v, _ in R])
    print([v for v, _ in RT])
    print([v for v, _ in C])
    print([v for v, _ in QT])

    print(len(set(tuple(v) for _, v in R)))
    print(len(set(v for _, v in C)))


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = solve(N, P, Q)
for row in ans:
    print("".join(map(str, row)))
