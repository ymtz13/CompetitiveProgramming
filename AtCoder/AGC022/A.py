from string import ascii_lowercase

S = input()

if len(S) == 26:
    for i in range(25, -1, -1):
        for j in range(25, i, -1):
            if S[i] < S[j]:
                print(S[:i] + S[j])
                exit()
    print(-1)

else:
    for c in ascii_lowercase:
        if c not in S:
            print(S + c)
            exit()
