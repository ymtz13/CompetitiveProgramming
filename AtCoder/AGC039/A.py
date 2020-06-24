S = input()
K = int(input())

w = None
N = []
for c in S:
    if c!=w:
        w=c
        N.append(1)
    else:
        N[-1]+=1

ans = 0
if len(N)==1:
    ans = (N[0]*K)//2
elif S[0]!=S[-1]:
    for n in N:
        ans += n//2
    ans *= K
else:
    ans += N[0]//2 + N[-1]//2
    ans += ((N[0]+N[-1])//2)*(K-1)
    for n in N[1:-1]:
        ans += (n//2)*K

print(ans)
