n, m = list(map(int, input().split()))
mod = 10**9+7

X = list(map(int, input().split()))
Dx = []
for i in range(n-1):
    Dx.append(X[i+1]-X[i])
#print(Dx)
S = [0]
for x in Dx:
    S.append((S[-1]+x) % mod)
#print(S)
T = [0]
for s in S:
    T.append((T[-1]+s) % mod)
#print(T)
Ux = 0
for i in range(1, n):
    Ux += (S[i]*i-T[i]) % mod
    #print(S[i]*i-T[i])

#print(Ux)

Y = list(map(int, input().split()))
Dy = []
for i in range(m-1):
    Dy.append(Y[i+1]-Y[i])
#print(Dy)
S = [0]
for y in Dy:
    S.append((S[-1]+y) % mod)
#print(S)
T = [0]
for s in S:
    T.append((T[-1]+s) % mod)
#print(T)
Uy = 0
for i in range(1, m):
    Uy += (S[i]*i-T[i]) % mod
    #print(S[i]*i-T[i])

#print(Uy)

print(Ux*Uy%mod)
