N = input()
S = input()
T = input()

print(len([s for s, t in zip(S, T) if s!=t]))
