S = input()

x=True
for c in S:
    x = x and S.count(c) == 2

print('Yes' if x else 'No')
