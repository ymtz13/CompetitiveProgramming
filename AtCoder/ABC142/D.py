A, B = list(map(int, input().split()))
if B>A: A,B = B,A
while B>0:
    A,B = B,A%B

p=2
ans=1
while p*2<=A:
    c=0
    while A%p==0:
        A//=p
        c+=1
    if c>0: ans+=1
    p+=1
if A>1: ans+=1

print(ans)
