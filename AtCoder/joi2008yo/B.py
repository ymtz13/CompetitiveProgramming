S = input()

a1 = a2 = 0
for i in range(len(S)):
    if S[i : i + 3] == "JOI":
        a1 += 1
    if S[i : i + 3] == "IOI":
        a2 += 1

print(a1)
print(a2)
