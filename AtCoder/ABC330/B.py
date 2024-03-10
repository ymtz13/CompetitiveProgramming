N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for a in A:
    ans.append(max(L, min(R, a)))

print(*ans)
