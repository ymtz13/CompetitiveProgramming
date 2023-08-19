def f(S):
    iA = [i for i, c in enumerate(S[:-1]) if c == "A"]
    iB = [i for i, c in enumerate(S[:-1]) if c == "B"]
    R = [S[i + 1] for i in iA] + [S[i + 1] for i in iB]
    return "".join(R)


def solve(S):
    while len(S) > 1:
        S = f(S)
    return S


print(f("ABAB"))
print(solve("ABAB"))

cA = cB = 0

for i in range(1 << 10):
    S = []
    for d in range(10):
        S.append("A" if i & (1 << d) else "B")
    S = "".join(S)

    ans = solve(S)
    if ans == "A":
        cA += 1
    else:
        cB += 1

    if ans == "B":
        print(S, solve(S))


print(cA, cB, cA + cB)
