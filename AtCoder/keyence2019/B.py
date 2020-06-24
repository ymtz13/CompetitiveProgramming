S = input()
for i in range(len(S)):
    for j in range(i, len(S)+1):
        if S[:i] + S[j:] == 'keyence':
            print('YES')
            exit()
print('NO')
