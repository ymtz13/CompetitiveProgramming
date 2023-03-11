N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

MAX = 16

Sset = set(S)

ConfirmedList = [[]]
freeus = MAX - sum(map(len, S)) - (N - 1) if N > 1 else 0

for q in range(N):
  ConfirmedList_next = []

  for Confirmed in ConfirmedList:
    used_freeus = sum([n - 1 for _, n in Confirmed])
    canuse = freeus - used_freeus + 1 if q < N - 1 else 0

    usedS = {ss for ss, _ in Confirmed}

    dict = {}
    for s in S:
      if s in usedS: continue
      for n in range(1 if q < N - 1 else 0, canuse + 1):
        ConfirmedList_next.append(Confirmed[:] + [(s, n)])

  ConfirmedList = ConfirmedList_next

Tset = set(T)

for Confirmed in ConfirmedList:
  ans = ''
  for ss, n in Confirmed:
    ans += ss + '_' * n

  if len(ans) < 3: continue

  if ans not in Tset:
    print(ans)
    exit()

print(-1)
