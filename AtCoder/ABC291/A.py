from string import ascii_uppercase

S = input()

for i, c in enumerate(S, 1):
  if c in ascii_uppercase:
    print(i)
    exit()