N = int(input())
S = []
for _ in range(N):
  S.append(tuple(map(int, input().split())))

ans = 0
for i, (t1, l1, r1) in enumerate(S):
  for t2, l2, r2 in S[i+1:]:
    ans += 1

    if not (r1 <= l2 or r2 <= l1): continue

    if t1==1: P1 = {l1, r1}
    if t1==2: P1 = {l1}
    if t1==3: P1 = {r1}
    if t1==4: P1 = set()

    if t2==1: P2 = {l2, r2}
    if t2==2: P2 = {l2}
    if t2==3: P2 = {r2}
    if t2==4: P2 = set()

    if P1 & P2: continue

    for p1 in P1:
      if l2 < p1 < r2: continue
    
    for p2 in P2:
      if l1 < p2 < r1: continue
    
    ans -= 1

print(ans)
