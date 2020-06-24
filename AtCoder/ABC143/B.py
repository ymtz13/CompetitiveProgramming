N = int(input())
D = list(map(int, input().split()))
ans = 0
for ix in range(N):
    for iy in range(ix+1, N):
        ans += D[ix]*D[iy]
print(ans)
