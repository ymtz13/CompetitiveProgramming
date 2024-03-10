N = int(input())
S = input()
Q = int(input())
Queries = [input().split() for _ in range(Q)]

ans = [None] * N

T = 0

Queries = [("1", i + 1, c) for i, c in enumerate(S)] + Queries

for t, x, c in reversed(Queries):
    if t == "1":
        x = int(x) - 1
        if ans[x] is not None:
            continue

        if T == "2":
            c = c.lower()
        if T == "3":
            c = c.upper()
        ans[x] = c

    else:
        if not T:
            T = t

print(*ans, sep="")
