N = int(input())
Called = [False] * (N + 1)
A = list(map(int, input().split()))

for i, a in enumerate(A, 1):
    if Called[i]:
        continue
    Called[a] = True

ans = [i for i, c in enumerate(Called[1:], 1) if not c]
print(len(ans))
print(*ans)
