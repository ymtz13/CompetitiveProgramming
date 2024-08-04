S = input()
ans = S[0] == "<" and S[-1] == ">" and S[1] == "=" and len(set(S[1:-1])) == 1
print("Yes" if ans else "No")
