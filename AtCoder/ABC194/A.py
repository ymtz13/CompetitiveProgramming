A, B = map(int, input().split())
C = A + B

def ans(C, B):
  if C>=15 and B>=8: return 1
  if C>=10 and B>=3: return 2
  if C>=3          : return 3
  return 4

print(ans(C, B))
