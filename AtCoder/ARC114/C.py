mod = 998244353

N, M = map(int, input().split())

DPCF = [[0] * (N + 1), [0] * (N + 1)]
DPCT = [[0] * (N + 1), [0] * (N + 1)]
DPWF = [[0] * (N + 1), [0] * (N + 1)]
DPWT = [[0] * (N + 1), [0] * (N + 1)]

dpCF = DPCF[-1]
dpCT = DPCT[-1]
dpWF = DPWF[-1]
dpWT = DPWT[-1]

dpCF[0] = 1
dpCT[1] = 1
dpWT[1] = 1

DPC = [[0] * (N + 1), [0] * (N + 1)]
DPW = [[0] * (N + 1), [0] * (N + 1)]
DPC[0][0] = 1
DPC[1][1] = 1
DPW[1][1] = 1

for n in range(2, N + 1):
  dpCF_next = [vf + vt for vf, vt in zip(dpCF, dpCT)]
  dpWF_next = [vf + vt for vf, vt in zip(dpWF, dpWT)]

  dpCT_next = [0] + [vf + vt for vf, vt in zip(dpCF[:-1], dpCT[:-1])]
  dpWT_next = [0] + [
      vf + vt + cf for vf, vt, cf in zip(dpWF[:-1], dpWT[:-1], dpCF[:-1])
  ]

  dpCF = dpCF_next
  dpCT = dpCT_next
  dpWF = dpWF_next
  dpWT = dpWT_next

  DPCF.append(dpCF)
  DPCT.append(dpCT)
  DPWF.append(dpWF)
  DPWT.append(dpWT)

  DPC.append([vf + vt for vf, vt in zip(dpCF, dpCT)])
  DPW.append([vf + vt for vf, vt in zip(dpWF, dpWT)])

  print()
  print('n = {}'.format(n))
  print('dpCF', dpCF)
  print('dpCT', dpCT)
  print('dpWF', dpWF)
  print('dpWT', dpWT)
  print('dpW', DPW[-1])

xC = [0]*(N+1)
xW = [0]*(N+1)
for _ in range(M):
  pass

print(xW)
print(xW[-1])
