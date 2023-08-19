N = int(input())
S = input()

s0 = set(S[0::2])
s1 = set(S[1::2])

if len(S) == 1:
    print("Yes")
    exit()

if len(s0) == 1 and len(s1) == 1 and S[0] != S[1]:
    print("Yes")
    exit()

print("No")
