from bisect import bisect_left

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

def dfs(A, B, x=31):
  if x < 0: return {0}
  if len(A) == 0 and len(B) == 0: return None

  b = 1 << x
  #tA = list(filter(lambda v: v & b, A))
  #tB = list(filter(lambda v: v & b, B))
  #fA = list(filter(lambda v: not v & b, A))
  #fB = list(filter(lambda v: not v & b, B))

  if len(A)<70:
    tA = []
    tB = []
    fA = []
    fB = []
    for v in A:
      if v&b: tA.append(v-b)
      else:   fA.append(v)
    for v in B:
      if v&b: tB.append(v-b)
      else:   fB.append(v)

  else:
    iA = bisect_left(A, b)
    iB = bisect_left(B, b)
    fA = A[:iA]
    fB = B[:iB]
    tA = [v - b for v in A[iA:]]
    tB = [v - b for v in B[iB:]]

  retval = None
  if len(tA) == len(tB):
    s1 = dfs(tA, tB, x - 1)
    s2 = dfs(fA, fB, x - 1)
    s = s1 & s2 if s1 is not None and s2 is not None else s1 or s2 or set()
    retval = s

  if len(tA) == len(fB):
    s3 = dfs(tA, fB, x - 1)
    s4 = dfs(fA, tB, x - 1)
    s = s3 & s4 if s3 is not None and s4 is not None else s3 or s4 or set()
    if retval is not None:
      retval |= {v + b for v in s}
    else:
      retval = {v + b for v in s}

  return retval or set()


ans = sorted(list(dfs(A, B)))

print(len(ans))
for a in ans:
  print(a)
