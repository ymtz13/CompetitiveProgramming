N = int(input())
C = [(0, ) + tuple(map(int, input().split())) for _ in range(1 << N)]

for n in range(N):
  Cnext = []
  for i in range(0, 1 << (N - n), 2):
    CL = C[i]
    CR = C[i + 1]

    cl0 = CL[0]
    cr0 = CR[0]
    cnext = tuple(max(cl + cr0, cr + cl0) for cl, cr in zip(CL[1:], CR[1:]))
    Cnext.append(cnext)
  
  C = Cnext

print(C[0][0])
