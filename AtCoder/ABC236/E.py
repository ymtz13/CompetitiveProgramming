N = int(input())
A = list(map(int, input().split()))


def check_avg(tgt):
  AA = [a - tgt for a in A]
  dp0 = dp1 = 0
  for a in AA:
    dp0_next = max(dp0, dp1) + a
    dp1 = dp0
    dp0 = dp0_next
  return max(dp0, dp1) >= 0


def check_mid(tgt):
  AA = [+1 if a >= tgt else -1 for a in A]
  dp0 = dp1 = 0
  for a in AA:
    dp0_next = max(dp0, dp1) + a
    dp1 = dp0
    dp0 = dp0_next
  return max(dp0, dp1) > 0


ok = 0
ng = 1 << 60
while ng - ok > 1e-4:
  tgt = (ok + ng) / 2

  if check_avg(tgt):
    ok = tgt
  else:
    ng = tgt

ans_avg = ok

ok = 0
ng = 1 << 60
while ng - ok > 1:
  tgt = (ok + ng) // 2

  if check_mid(tgt):
    ok = tgt
  else:
    ng = tgt

ans_mid = ok

print(ans_avg)
print(ans_mid)
