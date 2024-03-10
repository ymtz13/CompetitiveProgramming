from bisect import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
# Queries = [tuple(map(int, input().split())) for _ in range(Q)]

S = list(set(A))
S.sort()
D = {a: i for i, a in enumerate(S)}
IA = [D[a] for a in A]
T = len(S)


M = 500
M = 3
Z = []
for i in range(500):
    l = i * M
    r = l + M
    Asub = A[l:r]
    if not Asub:
        break
    IAsub = IA[l:r]

    z = [0] * T
    for a, ia in zip(Asub, IAsub):
        z[ia] += a

    for i in range(1, T):
        z[i] += z[i - 1]

    Z.append(z)


ans = []
prev = 0
# for L, R, X in Queries:
for _ in range(Q):
    L, R, X = tuple(map(int, input().split()))
    # L ^= prev
    # R ^= prev
    # X ^= prev
    # print(">", L, R, X)

    L -= 1
    l = (L + M - 1) // M
    r = R // M
    # print(f"L:{L}, l:{l*M}, r:{r*M}, R:{R}")

    aL = aR = aC = 0
    if l <= r:
        for a in A[L : l * M]:
            if a <= X:
                aL += a
        for a in A[r * M : R]:
            if a <= X:
                aR += a

        j = bisect(S, X)
        # print(f"j: {j}, S: {S}, X: {X}")
        if j:
            for z in Z[l:r]:
                # print(f"z:{z}")
                aC += z[j - 1]

    else:
        for a in A[L:R]:
            if a <= X:
                aL += a

    # print("=", aL, aC, aR)
    a = aL + aC + aR

    print(a)
    ans.append(a)
    prev = a

for a in ans:
    print(a)
