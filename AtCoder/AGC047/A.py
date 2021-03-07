N = int(input())
B = []
X = [[0]*19 for _ in range(19)]

for _ in range(N):
    s = input()
    if '.' not in s: s = s+'.0'
    a1, a2 = s.split('.')
    a2 = a2 + '0'*(9-len(a2))
    A = int(a1)*10**9 + int(a2)

    d2 = d5 = 0
    while A%2==0:
        A//=2
        d2+=1
    d2 = min(18, d2)

    while A%5==0:
        A//=5
        d5+=1
    d5 = min(18, d5)

    B.append((d2,d5))
    X[d2][d5] += 1

C = [[0]*19 for _ in range(19)]
for n2 in range(19):
    s = 0
    for n5 in range(18, -1, -1):
        s += X[n2][n5]
        C[n2][n5] = s

D = [[0]*19 for _ in range(19)]
for n5 in range(19):
    s = 0
    for n2 in range(18, -1, -1):
        s += C[n2][n5]
        D[n2][n5] = s

ans = 0
for n2, n5 in B:
    if n2*2>=18 and n5*2>=18: ans-=1
    ans += D[18-n2][18-n5]
    
print(ans//2)
