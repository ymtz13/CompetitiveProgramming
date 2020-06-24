N = int(input())
S = input()
ans = []
for c in S:
    x = (ord(c)-ord('A')+N) % 26 + ord('A')
    ans.append(chr(x))
print(''.join(ans))
