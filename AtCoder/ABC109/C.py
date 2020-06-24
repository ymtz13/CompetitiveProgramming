N, X = list(map(int, input().split()))
P = [abs(int(c)-X) for c in input().split() if int(c)-X !=0 ]

for i in range(len(P)-1):
    a, b = P[i], P[i+1]
    if a>b: a,b = b,a
    while a>0:
        a, b = b%a, a
    P[i+1]=b

print(P[-1])
