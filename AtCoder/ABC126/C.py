N, K = [int(c) for c in input().split()]

prob = 0

s = 1
while N*s<K:
    s*=2

t = 0
for i in range(N,0,-1):
    if i*s>=K:
        t+=1
    else:
        s*=2
        t=t*2+1
        
print('{:.10f}'.format(t/s/N))

