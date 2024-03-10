from collections import deque

N, L, D = map(int, input().split())

P = [1]
S = [0, 1]

for n in range(1, N + D + 5):
    l = max(0, n - D)
    r = min(L - 1, n - 1) + 1
    if l >= r:
        p = 0
    else:
        p = (S[r] - S[l]) / D

    P.append(p)
    S.append(S[-1] + p)

# print(P)

ans = [0] * (N + D + 5)
queue = deque([0] * D)
ss = 0
for n in range(N, -1, -1):
    # やめる場合の勝率
    p_lose = S[N + 1] - S[max(L, n)]
    p0 = 1 - p_lose

    # 続ける場合の勝率
    p1 = ss / D

    pp = max(p0, p1)
    ans[n] = pp
    queue.append(pp)
    ss += pp - queue.popleft()

print(ans[0])
