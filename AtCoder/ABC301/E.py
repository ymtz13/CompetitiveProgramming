from collections import deque

H, W, T = map(int, input().split())
H2 = H + 2
W2 = W + 2
N = H2 * W2
B = [0] * N

iX = []

for h in range(1, H + 1):
    A = input()
    for w, a in enumerate(A, 1):
        if a == "#":
            continue
        i = h * W2 + w
        B[i] = 1

        if a == "S":
            iS = i
        if a == "G":
            iG = i
        if a == "o":
            iX.append(i)

INF = 1 << 60

iX = iX + [iS, iG]
M = len(iX)

D = [[INF] * M for _ in range(M)]

for ist, st in enumerate(iX):
    dist = [INF] * N

    queue = deque([st])
    while queue:
        q = queue.popleft()
        d = q // N
        i = q % N

        if dist[i] != INF:
            continue
        dist[i] = d

        if B[i - W2]:
            queue.append(q + N - W2)
        if B[i + W2]:
            queue.append(q + N + W2)
        if B[i - 1]:
            queue.append(q + N - 1)
        if B[i + 1]:
            queue.append(q + N + 1)

    for igl, gl in enumerate(iX):
        D[ist][igl] = dist[gl]

if D[-2][-1] > T:
    print(-1)
    exit()

K = len(D) - 2  # num of sweets
dp = [INF] * (1 << K) * K

# for row in D:
#     print(row)

for k in range(K):
    dp[(1 << k) * K + k] = D[K][k]  # start -> k


def print_dptable(dp):
    for i, v in enumerate(dp):
        if v < INF:
            print("{} dist:{}".format(print_state(i), v))


def print_state(state):
    history = state // K
    node = state % K
    return "{:02b} {}".format(history, node)


for history_to in range(1, 1 << K):
    nodes = []
    for i in range(K):
        if history_to & (1 << i):
            nodes.append(i)

    # print(nodes)

    for t in nodes:
        bit_to = 1 << t
        state_to = history_to * K + t
        history_from = history_to - bit_to

        for f in nodes:
            if f == t:
                continue
            state_from = history_from * K + f
            # print(
            #     print_state(state_from),
            #     print_state(state_to),
            # )

            dp[state_to] = min(dp[state_to], dp[state_from] + D[f][t])

# print_dptable(dp)

dist_gl = D[-1]
ans = 0

for state, dist in enumerate(dp):
    history = state // K
    node = state % K

    if dist + dist_gl[node] > T:
        continue

    popcount = 0
    for i in range(K):
        if history & (1 << i):
            popcount += 1

    ans = max(ans, popcount)

print(ans)
