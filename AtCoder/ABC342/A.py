S = list(input())
SS = sorted(S)
C = SS[0] if SS[0] != SS[1] else SS[-1]

for i, c in enumerate(S, 1):
    if c == C:
        print(i)
