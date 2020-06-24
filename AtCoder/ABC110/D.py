N, M = list(map(int, input().split()))

if M==1:
    print(1)
    exit()

C = [1] # (N+K-1, N-1) K=0,1,2,...,30
for k in range(1,31):
    C.append(C[-1]*(k+N-1)//k)

F = {}
f = 2
while f*f<=M and M>1:
    if M%f==0:
        if f in F: F[f] += 1
        else: F[f] = 1
        M//=f
    else:
        f+=1

if M in F: F[M]+=1
else: F[M]=1

d = 1
for f, k in F.items():
    d *= C[k]

print(d%1000000007)
