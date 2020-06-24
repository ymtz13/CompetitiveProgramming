N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
s = A1[0] + sum(A2)
ans = s
for i in range(1,N):
    s+=A1[i]-A2[i-1]
    ans = max(ans, s)
print(ans)
