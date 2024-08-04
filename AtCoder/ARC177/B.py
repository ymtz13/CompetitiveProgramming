N = int(input())
S = input()

ans = []
for i in range(N - 1, -1, -1):
    if S[i] == "0":
        continue

    ans.extend(["A"] * (i + 1))
    ans.extend(["B"] * i)

print(len(ans))
print("".join(ans))
