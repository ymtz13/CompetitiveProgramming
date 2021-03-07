N = int(input())
p = 1
ans1 = []
ans2 = []
while p*p<N:
    if N%p==0:
        ans1.append(p)
        ans2.append(N//p)
    p+=1

if p*p==N: ans1.append(p)

for a in ans1:
    print(a)
for a in reversed(ans2):
    print(a)
