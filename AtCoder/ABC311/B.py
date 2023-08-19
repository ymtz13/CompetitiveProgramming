N, D = map(int, input().split())
S = [input() for _ in range(N)]

X = ["x" not in x for x in zip(*S)]

T = "".join(["o" if x else "x" for x in X])

Z = [len(t) for t in T.split("x")]
print(max(Z))
