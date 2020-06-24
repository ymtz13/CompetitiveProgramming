S, T = input(), input()
M = [[0]*26 for _ in range(26)]
a = ord('a')

for s,t in zip(S,T):
    M[ord(s)-a][ord(t)-a]=1

f = True
for i in range(26):
    sr, sc = 0, 0
    for j in range(26):
        sr += M[i][j]
        sc += M[j][i]

    if sr>1 or sc>1:
        f = False
        break

print('Yes' if f else 'No')
