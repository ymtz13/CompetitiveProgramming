N = int(input())
A = list(map(int, input().split()))
p = A[0]
ans = 0
for a in A[1:]:
    ans += max(0, p-a)
    p = max(p,a)
print(ans)
