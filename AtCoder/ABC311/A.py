N = int(input())
S = input()

s = set()
for i, c in enumerate(S, 1):
    s.add(c)
    if len(s) == 3:
        print(i)
        exit()
