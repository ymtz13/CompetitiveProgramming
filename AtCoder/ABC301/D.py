S = input()
N = int(input())

M = 60

S = "0" * (M - len(S)) + S
S = list(S)

Q = [i for i, c in enumerate(S) if c == "?"]

for i in range(M):
    if S[i] == "?":
        S[i] = 0
    else:
        S[i] = int(S[i])


B = []
for i in range(60):
    B.append((N >> i) & 1)
B = B[::-1]


def calc(S):
    r = 0
    for i, v in enumerate(reversed(S)):
        r += v << i
    return r


for q in Q:
    SS = S[:]
    SS[q] = 1

    x = calc(SS)

    if x <= N:
        S[q] = 1

ans = calc(S)
print(ans if ans <= N else -1)
