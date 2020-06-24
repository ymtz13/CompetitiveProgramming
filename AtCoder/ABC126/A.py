N, K = [int(c) for c in input().split()]
S = input()

O = ''
for i,c in enumerate(S):
    O += c if i+1 != K else c.lower()

print(O)
