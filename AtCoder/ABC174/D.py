N = int(input())
C = list(input())
nR = C.count('R')
nW = N - nR

mR = 0
for c in C[:nR]:
    if c=='W': mR += 1

print(mR)
