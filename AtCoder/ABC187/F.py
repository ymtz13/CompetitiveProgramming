N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
NV = [set() for _ in range(N)]
for a, b in AB:
  NV[a-1].add(b-1)
  NV[b-1].add(a-1)

C = []
def BK(R, P, X):
  if not P and not X:
    C.append(R)
    return

  u = list(P|X)[0]
  for v in P - NV[u]:
    BK(R | {v}, P & NV[v], X & NV[v])
    P = P - {v}
    X = X | {v}

BK(set(), set(range(N)), set())

L = len(C)

def dfs(i, n, v):
  if len(v)==N: return n
  if i==L: return 100

  return min(dfs(i+1, n, v), dfs(i+1, n+1, v | C[i]))

print(dfs(0, 0, set()))
