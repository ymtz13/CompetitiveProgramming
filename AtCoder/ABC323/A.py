S = input()
X = [v for v in S[1::2] if v != "0"]
print("Yes" if not X else "No")
