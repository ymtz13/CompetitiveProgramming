input()
V = [int(c) for c in input().split()]
C = [int(c) for c in input().split()]

S = 0
for v,c in zip(V,C):
    if v>c : S+=v-c
print(S)
