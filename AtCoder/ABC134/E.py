import bisect

N = int(input())
A = [-int(input()) for _ in range(N)]

x = [A[0]]

for a in A[1:]:
    i = bisect.bisect(x,a)
    if i==len(x): x.append(a)
    else: x[i]=a

print(len(x))
