S = input()
ans = []
for c0, c1 in zip(S[0::2], S[1::2]):
    ans.extend([c1, c0])
print("".join(ans))
