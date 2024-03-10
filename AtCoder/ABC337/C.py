N = int(input())
A = [0] + list(map(int, input().split()))

Next = [None] * (N + 1)

for i, a in enumerate(A):
    if a == -1:
        s = i
    else:
        Next[a] = i


ans = []
for _ in range(N):
    ans.append(s)
    s = Next[s]

print(*ans)
