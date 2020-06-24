s=0
u=10
for t in [int(input()) for _ in range(5)]:
    m=t%10
    n=1 if m>0 else 0
    s+=(t//10+n)*10
    if n==1 and m<u : u=m

if u<10:s-=10-u
print(s)
