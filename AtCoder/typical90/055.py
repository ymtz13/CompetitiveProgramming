N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for iv, v in enumerate(A):
  pv = v
  for iw, w in enumerate(A[iv+1:], iv+1):
    pw = pv * w % P
    for ix, x in enumerate(A[iw+1:], iw+1):
      px = pw * x % P
      for iy, y in enumerate(A[ix+1:], ix+1):
        py = px * y % P
        for iz, z in enumerate(A[iy+1:], iy+1):
          pz = py * z % P
          if pz==Q: ans += 1

print(ans)
