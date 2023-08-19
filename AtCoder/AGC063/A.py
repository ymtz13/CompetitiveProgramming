N = int(input())
S = input()

INF = N + 3

Ai = [i for i, c in enumerate(S) if c == "A"] + [INF] * N
Bi = [i for i, c in enumerate(S) if c == "B"] + [INF] * N

# print(Ai, Bi)

mex = 0
marked = [False] * (N + 5)

ans = []

for k in range(1, N + 1):
    kA = (k + 1) // 2
    kB = k - kA

    nA = Bi[kA - 1]
    nB = Ai[kB - 1] if kB > 0 else -1

    marked[nA] = True
    if nB != -1:
        marked[nB] = True

    while marked[mex]:
        mex += 1

    ans.append(S[mex] == "A")


for a in ans:
    print("Alice" if a else "Bob")
