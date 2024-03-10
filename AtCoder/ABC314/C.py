from collections import deque

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

Z = [deque() for _ in range(M + 1)]
for s, c in zip(S, C):
    Z[c].append(s)

for z in Z[1:]:
    z.appendleft(z.pop())

ans = []
for c in C:
    ans.append(Z[c].popleft())

print(*ans, sep="")
