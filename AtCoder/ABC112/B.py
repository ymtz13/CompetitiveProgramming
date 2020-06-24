N, T = list(map(int, input().split()))
C = []
for n in range(N):
    c, t = list(map(int, input().split()))
    if t<=T: C.append(c)

print(min(C) if C else 'TLE')
