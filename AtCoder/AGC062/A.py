T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    S = input()

    j = -1
    for i, c in enumerate(S):
        if c == "B":
            j = i
            break

    if j == -1:
        ans.append("A")
        continue

    s1 = set(S[:j])
    s2 = set(S[j:])
    if len(s1) <= 1 and len(s2) == 1:
        ans.append("B")
    else:
        ans.append("A")


for a in ans:
    print(a)
