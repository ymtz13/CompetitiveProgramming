S = input()

ss = set()
for f in range(len(S)):
    for t in range(f + 1, len(S) + 1):
        ss.add(S[f:t])

print(len(ss))
