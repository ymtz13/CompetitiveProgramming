S = input()
T = input()

R = [(ord(t) - ord(s)) % 26 for s, t in zip(S, T)]

print('Yes' if len(set(R)) == 1 else 'No')
