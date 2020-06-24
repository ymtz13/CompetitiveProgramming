N = int(input())
A = sorted(list(map(int, input().split())))
M = 1000001
D = [False]*M
ans = 0
for i, a in enumerate(A):
    if not D[a]:
        if i==N-1 or A[i+1]>a : ans += 1
        b = a
        while b<M:
            D[b] = True
            b += a



print(ans)
            

