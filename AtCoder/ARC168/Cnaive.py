N, K = map(int, input().split())
S = input()

Pair = [(l, r) for l in range(N - 1) for r in range(l + 1, N)]

s = [{S}]
for _ in range(K):
    snext = set()
    for z in s[-1]:
        for l, r in Pair:
            t = list(z)
            t[l], t[r] = t[r], t[l]
            snext.add("".join(t))

    s.append(snext)

print(s)

b = [set()]
for z in s:
    b.append(b[-1] | z)
b = b[1:]

for k, bb in enumerate(b):
    print(k, len(bb), bb)

print(b[4] - b[3])
