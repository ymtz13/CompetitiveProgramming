N = input()
S = 0
for c in N:
    S += int(c)
print('Yes' if int(N)%S==0 else 'No')
