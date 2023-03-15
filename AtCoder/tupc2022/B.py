N, M, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)] + [(N + 1, -1)]

h = d = 0
ans = 0
for i, (a, b) in enumerate(AB):
    if i == M:
        break

    h = max(0, h - (a - d)) + b
    d = a

    anext = AB[i + 1][0]

    ans += min(anext - a, max(0, h - K))

print(ans)
