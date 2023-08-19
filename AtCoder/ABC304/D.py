from bisect import bisect
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())
PQ = [tuple(map(int, input().split())) for _ in range(N)]

nA = int(input())
A = [0] + list(map(int, input().split())) + [W]
nB = int(input())
B = [0] + list(map(int, input().split())) + [H]

D = defaultdict(int)
for p, q in PQ:
    pp = A[bisect(A, p)]
    qq = B[bisect(B, q)]
    D[(pp, qq)] += 1

values = list(D.values())
if len(values) < (nA + 1) * (nB + 1):
    values.append(0)

print(min(values), max(values))
