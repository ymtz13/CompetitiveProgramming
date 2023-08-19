from bisect import bisect

N, Q = map(int, input().split())
A = [-v for v in map(int, input().split())]
A.sort()
ans = []

for _ in range(Q):
    x = int(input())
    ans.append(bisect(A, -x))

for a in ans:
    print(a)
