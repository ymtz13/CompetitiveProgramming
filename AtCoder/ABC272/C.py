import re

N = int(input())
A = list(map(int, input().split()))
A0 = sorted([a for a in A if a % 2 == 0], reverse=True)
A1 = sorted([a for a in A if a % 2 == 1], reverse=True)

ans0 = -1 if len(A0) < 2 else sum(A0[:2])
ans1 = -1 if len(A1) < 2 else sum(A1[:2])
print(max(ans0, ans1))
