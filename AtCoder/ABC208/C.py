N, K = map(int, input().split())
A = sorted([(a, i) for i, a in enumerate(map(int, input().split()))])

ans = [K//N]*N
R = K%N
for a, i in A[:R]:
  ans[i] += 1

for a in ans:
  print(a)
