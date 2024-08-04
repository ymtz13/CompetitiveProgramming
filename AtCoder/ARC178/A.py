N, M = map(int, input().split())
A = set(map(int, input().split()))

if 1 in A or N in A:
    print(-1)
    exit()

ans = [1]
p = None
for n in range(2, N + 1):
    if n in A:
        ans.append(n + 1)
        if p is None:
            p = n
    else:
        if p is None:
            ans.append(n)
        else:
            ans.append(p)
            p = None

print(*ans)
