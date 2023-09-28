N = int(input())
M = int(input())
T = list(map(int, input().split()))
S = [0] * (N + 1)

for t in T:
    B = list(map(int, input().split()))

    x = N
    for i, b in enumerate(B, 1):
        if b == t:
            S[i] += 1
            x -= 1
    S[t] += x


for s in S[1:]:
    print(s)
