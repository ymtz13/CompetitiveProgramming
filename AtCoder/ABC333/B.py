S1, S2 = [ord(c) - ord("A") for c in input()]
T1, T2 = [ord(c) - ord("A") for c in input()]

dS = min(abs(S1 - S2), 5 - abs(S1 - S2))
dT = min(abs(T1 - T2), 5 - abs(T1 - T2))

print("Yes" if dS == dT else "No")
