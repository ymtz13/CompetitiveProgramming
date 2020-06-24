import sys
input = sys.stdin.readline

N = int(input())
S, _ = input()+'_', input()

A = []

i=0
while i<N:
    if S[i]!=S[i+1]:
        A.append(1)
        i+=1
    else:
        A.append(2)
        i+=2

p = A[0]
ans = 3 if p==1 else 6
mod = 10**9+7
for a in A[1:]:
    if p==1 and a==1: d=2
    if p==1 and a==2: d=2
    if p==2 and a==1: d=1
    if p==2 and a==2: d=3
    ans = (ans*d)%mod
    p = a

print(ans)
