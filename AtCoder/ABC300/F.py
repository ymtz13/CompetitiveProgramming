N, M, K = map(int, input().split())
S = input()

nx = S.count('x')
k = max(0, K//nx-1)

ans = N*k
K -= nx*k

S = S*min(3, M-k)

Z = [0]
for c in S:
    Z.append(Z[-1]+(1 if c=='x' else 0))

l = m = 0
for r, zr in enumerate(Z[1:], 1):
    while zr-Z[l]>K:
        l+=1
    m = max(m,r-l)

print(ans+m)


