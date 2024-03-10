N = int(input())
D = list(map(int, input().split()))

ans = 0
for n, dmax in enumerate(D, 1):
    for d in range(1, dmax + 1):
        s = set(f"{n}{d}")
        if len(s) == 1:
            ans += 1

print(ans)
