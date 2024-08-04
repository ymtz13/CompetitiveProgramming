S = input()
T = input()

i = 0
ans = []
for j, t in enumerate(T):
    if S[i] == t:
        i += 1
        ans.append(j + 1)
        if i == len(S):
            break

print(*ans)
