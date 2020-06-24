N = int(input())
A = list(map(int, input().split()))
C = set()
R = 0
for a in A:
    c = a//400 if a<3200 else 8
    C.add(c)
    if c==8: R+=1

print(len(C) - min(1, R, len(C)-1), len(C) + max(0, R-1))
