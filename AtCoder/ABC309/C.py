N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True)

s = 0
for a, b in AB:
    s += b
    if s > K:
        print(a + 1)
        exit()

print(1)
