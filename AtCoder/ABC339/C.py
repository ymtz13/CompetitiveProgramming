N = int(input())
A = list(map(int, input().split()))

S = [0]
for a in A:
    S.append(S[-1] + a)

print(S[-1] - min(S))
