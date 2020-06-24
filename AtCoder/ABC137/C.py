N = int(input())
S = sorted([''.join(sorted(input())) for _ in range(N)])
print(S)
prev = ''
ans = 0
n = 0
for i in range(N):
    if S[i]!=prev:
        ans += n*(n-1)//2
        prev=S[i]
        n=1
    else:
        n+=1
ans += n*(n-1)//2

print(ans)
