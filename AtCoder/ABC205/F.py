from collections import deque

H, W, N = map(int, input().split())
ABCD = [tuple(map(int, input().split())) for _ in range(N)]

ST = 0
GL = 1

# node
# start : 0
# goal  : 1
# h     : h+1
# w     : w+H+1
# n     : 2*n+H+W -> 2*n+H+W+1

edges = []
capacity = []

for h in range(1, H + 1):
    edges.append((ST, h + 1))
    edges.append((h + 1, ST))
    capacity.append(1)
    capacity.append(0)

for w in range(1, W + 1):
    edges.append((w + H + 1, GL))
    edges.append((GL, w + H + 1))
    capacity.append(1)
    capacity.append(0)

for n, (A, B, C, D) in enumerate(ABCD, 1):
    nf = 2 * n + H + W
    nt = nf + 1

    edges.append((nf, nt))
    edges.append((nt, nf))
    capacity.append(1)
    capacity.append(0)

    for h in range(A, C + 1):
        edges.append((h + 1, nf))
        edges.append((nf, h + 1))
        capacity.append(1)
        capacity.append(0)

    for w in range(B, D + 1):
        edges.append((nt, w + H + 1))
        edges.append((w + H + 1, nt))
        capacity.append(1)
        capacity.append(0)

M = 2 * N + H + W + 2
E = [[] for _ in range(M)]

for i, (f, t) in enumerate(edges):
    E[f].append((t, i))

ans = 0

while True:
    queue = deque([(0, -1, -1)])
    prev = [None] * M

    while queue:
        q, p, j = queue.popleft()
        if prev[q] is not None:
            continue
        prev[q] = (p, j)

        for e, i in E[q]:
            if capacity[i] > 0:
                queue.append((e, q, i))

    if prev[GL] is None:
        print(ans)
        exit()

    ans += 1

    x = GL
    while x != -1:
        p, j = prev[x]

        k = j - 1 if j % 2 else j + 1
        capacity[j] -= 1
        capacity[k] += 1

        x = p
