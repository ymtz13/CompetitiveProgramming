from collections import deque

N, L = map(int, input().split())

X = [deque(), deque()]
T = [0]
S = 0

for i in range(N):
    A = int(input())
    if S + A > L:
        X.append(deque())
        T.append(S)
        S = 0
    X[-1].append((i, A))
    S += A

T.append(S)

print(X)
print(T)
ans = [None] * N

for j, x in enumerate(X[1:], 1):
    i, _ = x[0]
    ans[i] = (len(X) - j, S)

while True:
    for i in range(len(X) - 1):
        if not X[i + 1]:
            break
        _, v = X[i + 1][0]

        if T[i] + v <= L:
            X[i].append(X[i + 1].popleft())
            T[i] += v
            T[i + 1] -= v
            k = i + 1

    X[0].clear()
    T[0] = 0

    print(k)
    print(X)
    print(T)
    input()

    if not X[0] or ans[X[0][0][0]] is not None:
        break


for a in ans:
    print(a)
