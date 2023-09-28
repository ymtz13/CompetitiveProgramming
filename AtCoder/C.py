from collections import deque

N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
S = ans = sum(F)

F = deque(F)

for n in range(N + 1):
    S += P
    if F:
        for _ in range(D):
            if F:
                S -= F.popleft()

    ans = min(ans, S)

print(ans)
