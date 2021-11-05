N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ia = ib = 0
ans = []
while ia < N and ib < M:
  a = A[ia]
  b = B[ib]
  if a==b:
    ia += 1
    ib += 1
    continue
  
  if a < b:
    ia += 1
    ans.append(a)
  else:
    ib += 1
    ans.append(b)

ans.extend(A[ia:])
ans.extend(B[ib:])
print(' '.join(map(str, ans)))
