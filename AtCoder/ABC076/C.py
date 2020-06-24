S = input()
T = input()
L = []

for i in range(len(S)-len(T)+1):
    ok = True
    for j, t in enumerate(T):
        if S[i+j]!=t and S[i+j]!='?':
            ok = False
            break
    if ok: L.append(i)

S = S.replace('?', 'a')
X = []
for i in L:
    X.append(S[:i] + T + S[i+len(T):])

print(min(X) if len(X)!=0 else 'UNRESTORABLE')
