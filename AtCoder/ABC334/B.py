A, M, L, R = map(int, input().split())

L -= A
R -= A

if L < 0:
    x = L // M
    L -= x * M
    R -= x * M


l = (L - 1) // M + 1
r = R // M + 1

print(r - l)
