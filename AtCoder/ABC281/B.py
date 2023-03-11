from string import ascii_uppercase


def ans(x):
  print('Yes' if x else 'No')
  exit()


S = input()
if len(S) != 8:
  ans(False)

a = S[0]
b = S[1:-1]
c = S[-1]

if a not in ascii_uppercase: ans(False)
if c not in ascii_uppercase: ans(False)

if set(b) & set(ascii_uppercase): ans(False)

if str(int(b)) != b: ans(False)

ans(True)
