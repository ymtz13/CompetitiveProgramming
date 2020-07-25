from bisect import bisect

N = int(input())
A = list(map(int, input().split()))
B = [[] for _ in range(max(A)+1)]

for i, a in enumerate(A):
    B[a].append(i)

x = -1
ans = 0
for b in B:
    if len(b)==0: continue
    i = bisect(b, x)
    if i==0:
        x = b[-1]
    else:
        x = b[i-1]
        ans += 1

if x>0: ans+=1
        
print(ans)
