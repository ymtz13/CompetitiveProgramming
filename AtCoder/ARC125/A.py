N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A[0] == 1:
  A = [1 - a for a in A]
  B = [1 - b for b in B]


def solve(A, B):
  if 1 not in B: return M
  if 1 not in A: return -1

  i1 = [i for i, a in enumerate(A) if a == 1]
  d = min(i1[0], N - i1[-1])

  ans = 0
  r = False
  p = 0
  for b in B:
    if b==p:
      ans += 1
    elif r:
      ans += 2
      p = b
    else:
      ans += d + 1
      p = b
      r = True
  
  return ans

print(solve(A, B))
