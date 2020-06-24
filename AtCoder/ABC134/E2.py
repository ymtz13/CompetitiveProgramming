import bisect

N = int(input())
A = [int(input()) for _ in range(N)]

x = []

for a in A:
    i = bisect.bisect_left(x,a)
    if i==0: x = [a] + x
    else: x[i-1]=a

print(len(x))
