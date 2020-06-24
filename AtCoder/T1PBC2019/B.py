N = input()
S = input()
K = int(input())

retval = ''
for c in S:
    retval += '*' if c!=S[K-1] else c

print(retval)
