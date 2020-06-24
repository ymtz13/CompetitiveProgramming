N = int(input())
P = list(map(int, input().split()))
diff = 0
for p,q in zip(P,list(range(1,N+1))):
    if p!=q : diff+=1

print('YES' if diff<=2 else 'NO')
