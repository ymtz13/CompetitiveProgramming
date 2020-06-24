N = int(input())
A = list(map(int, input().split()))
S = sum(A)
T = 0
ans = 10**20
for a in A[:-1]:
    T += 2*a
    ans = min(ans, abs(T-S))
print(ans)
