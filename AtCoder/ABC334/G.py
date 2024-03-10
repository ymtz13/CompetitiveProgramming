from collections import deque

mod = 998244353

RED = 0
GREEN = 1

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2

S = [2] * (H2 * W2)
green = 0
for h in range(1, H + 1):
    for w, c in enumerate(input(), 1):
        i = h * W2 + w
        c = RED if c == "." else GREEN
        S[i] = c

        if c == GREEN:
            green += 1

ord = [-1] * (H2 * W2)
low = [1 << 60] * (H2 * W2)
childs = [[] for _ in range(H2 * W2)]

cnt = 0

for hs in range(1, H + 1):
    for ws in range(1, W + 1):
        st = hs * W2 + ws
        stack = deque([(st, None)])

        o = 0
        visited = []
        while stack:
            q, p = stack.pop()

            if S[q] != GREEN or ord[q] != -1:
                continue
            ord[q] = o
            o += 1

            visited.append(q)
            if p is not None:
                childs[p].append(q)

            stack.append((q - 1, q))
            stack.append((q + 1, q))
            stack.append((q - W2, q))
            stack.append((q + W2, q))

        if visited:
            cnt += 1

        for q in reversed(visited):
            ordq = ord[q]
            l = ordq
            P = []
            for e in (q + 1, q - 1, q + W2, q - W2):
                if ord[e] > ord[q]:
                    l = min(l, low[e])
                elif ord[e] >= 0:
                    P.append(ord[e])

            if len(P) >= 2:
                l = min(l, min(P))

            low[q] = l

Z = [0, 0, 0, 0, 0]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        q = h * W2 + w
        if S[q] != GREEN:
            continue

        ordq = ord[q]

        c = 0 if ordq > 0 else -1
        # for e in (q + 1, q - 1, q + W2, q - W2):
        for e in childs[q]:
            if low[e] >= ordq:
                c += 1

        # print((h, w), c)
        Z[c + 1] += 1

# print("ord")
# for h in range(1, H + 1):
#     v = [v if v >= 0 else " " for v in ord[W2 * h + 1 : W2 * h + W2 - 1]]
#     print(*v)
# print("low")
# for h in range(1, H + 1):
#     v = [v if v < 10000 else " " for v in low[W2 * h + 1 : W2 * h + W2 - 1]]
#     print(*v)


# print(cnt, Z)

inv = pow(green, mod - 2, mod)
ans = 0
for c, v in enumerate(Z, cnt - 1):
    ans += c * v * inv % mod
    ans %= mod

print(ans)
