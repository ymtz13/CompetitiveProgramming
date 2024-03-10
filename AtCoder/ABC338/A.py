from string import ascii_lowercase, ascii_uppercase

S = input()

a = S[0] in ascii_uppercase
b = all([c in ascii_lowercase for c in S[1:]])

print("Yes" if a and b else "No")
