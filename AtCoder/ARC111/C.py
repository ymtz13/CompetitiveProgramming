N = int(input())
A = list(map(int, input().split()))
B = [(b, ib) for ib, b in enumerate(map(int, input().split()))]
P = [p - 1 for p in map(int, input().split())]

Pinv = [None] * N  # 荷物ib は 人Pinv[ib] が持っている
for i, p in enumerate(P):
  Pinv[p] = i

ans = []

for b, ib in sorted(B, reverse=True):
  # 人Pinv[ib] が持っている 荷物ib と
  # 人ib が持っている 荷物P[ib] を交換する

  #print('P', P)
  #print('Pinv', Pinv)

  ia1 = Pinv[ib]
  ib1 = ib
  ia2 = ib
  ib2 = P[ib]

  if ia1 == ia2: continue
  if A[ia1] <= B[ib1][0] or A[ia2] <= B[ib2][0]:
    print(-1)
    exit()

  P[ia1] = ib2
  P[ia2] = ib1
  Pinv[ib1] = ia2
  Pinv[ib2] = ia1
  ans.append((ia1 + 1, ia2 + 1))

print(len(ans))
for a in ans:
  print(*a)

# [(1, 2), (3, 3), (3, 1), (5, 0)]

# [(5, 0), (3, 3), (3, 1), (1, 2)]

# [(5, 0), (1, 2), (3, 1), (3, 3)]

# [(5, 0), (3, 1), (1, 2), (3, 3)]
