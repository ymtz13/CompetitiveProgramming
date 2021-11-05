H, W, N = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]
SH = {A for A, _ in C}
SW = {B for _, B in C}

DH = {A: i for i, A in enumerate(sorted(list(SH)), 1)}
DW = {B: i for i, B in enumerate(sorted(list(SW)), 1)}

for A, B in C:
  print(DH[A], DW[B])
