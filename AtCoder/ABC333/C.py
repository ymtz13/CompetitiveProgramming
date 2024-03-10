N = int(input())
X = []

S = set()
for n1 in range(1, 13):
    v1 = int("1" * n1)
    for n2 in range(1, 13):
        v2 = int("1" * n2)
        for n3 in range(1, 13):
            v3 = int("1" * n3)
            S.add(v1 + v2 + v3)

S = list(S)
S.sort()
print(S[N - 1])
