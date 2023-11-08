N, K = map(int, input().split())
S = input()

INF = 1 << 60

dp = [[INF, INF, 0]]

for c in S:
    vR, vG, vB = dp[-1]
    nxt = [vR + 1, vG + 1, vB + 1]

    if c == "R":
        nxt[0] = min(nxt[0], ((vB + K - 1) // K) * K)
    if c == "G":
        nxt[1] = min(nxt[1], ((vR + K - 1) // K) * K)
    if c == "B":
        nxt[2] = min(nxt[2], ((vG + K - 1) // K) * K)

    dp.append(nxt)

# for c, v in zip("_" + S, dp):
#     print(c, v)

print(((dp[-1][2] + K - 1) // K))
