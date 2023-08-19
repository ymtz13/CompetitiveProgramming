from collections import deque

N, M = map(int, input().split())
TT = [[], [], []]

for _ in range(N):
    T, X = map(int, input().split())
    TT[T].append(X)

T0, T1, T2 = TT

T0 = T0 + [0] * (M - len(T0))
T0 = sorted(T0, reverse=True)[:M]
T0.reverse()

T1.sort(reverse=True)
T1.append(0)

T2.sort(reverse=True)


ans = s = sum(T0)

K = 0
k = 0
T0 = deque(T0)

for t2 in T2:
    if not T0:
        print(ans)
        exit()

    v = T0.popleft()
    s -= v
    K += t2

    for i in range(k, min(K, len(T1))):
        if not T0:
            print(ans)
            exit()

        v = T0.popleft()
        w = T1[i]

        if v >= w:
            print(ans)
            exit()

        s += w - v
        ans = max(ans, s)

print(ans)
