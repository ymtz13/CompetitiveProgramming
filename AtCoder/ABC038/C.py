N = int(input())
A = list(map(int, input().split()))
p = 0
ans = 1
for i in range(1, N):
    if A[i]<=A[i-1]:
        p = i
    ans += i-p+1

print(ans)
