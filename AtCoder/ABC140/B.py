N = int(input())
A = list(map(int, input().split()))
ans = sum(list(map(int, input().split())))
C = list(map(int, input().split()))

for i, a in enumerate(A[:-1]):
    if A[i+1] == a+1: ans+=C[a-1]

print(ans)
