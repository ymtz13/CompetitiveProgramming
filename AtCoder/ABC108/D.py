L = t = int(input())
X = []
B = 4
while L:
    X.append(L%B)
    L//=B

E = []
N = len(X)*2
for i, x in enumerate(X[:-1]):
    r = B**i
    #s = x+1 if i==0 else x
    s = x
    t -= r*x
    for k in range(0, s):
        E.append((2*i+1, 2*i+2, r*k))

    E.append((2*i+2, 2*i+3, 0))

    for k in range(s, B):
        E.append((2*i+1, 2*i+3, r*k))

    E.append((2*i+2, N, t))

for k in range(0, X[-1]):
    E.append((N-1, N, B**(len(X)-1)*k))

print(N, len(E))
for e in E:
    print(*e)
