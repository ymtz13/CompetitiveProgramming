from collections import deque

N = int(input())
N2 = N + 2
M = N2 * N2
Msq = M * M

S = [0] * (N2 * N2)
P = []

for h in range(1, N + 1):
    s = input()
    for w, c in enumerate(s, 1):
        i = h * N2 + w
        if c == "P":
            P.append(i)
        if c != "#":
            S[i] = 1

p1, p2 = P

queue = deque([p1 * M + p2])
dist = [-1] * Msq
while queue:
    q = queue.popleft()
    d, q = q // Msq, q % Msq
    if dist[q] != -1:
        continue
    dist[q] = d
    d1 = d + 1

    q1, q2 = q // M, q % M

    for e in (-N2, N2, -1, 1):
        r1 = q1 + e
        r2 = q2 + e

        t1 = r1 if S[r1] else q1
        t2 = r2 if S[r2] else q2

        queue.append(d1 * Msq + t1 * M + t2)

INF = 1 << 60
ans = INF
for i in range(M):
    d = dist[i * M + i]
    if d != -1:
        ans = min(ans, d)

print(ans if ans < INF else -1)
