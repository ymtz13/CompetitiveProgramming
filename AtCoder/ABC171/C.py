N = int(input())-1
ans = []
while True:
    x = N%26
    N //= 26
    N -= 1
    ans.append(chr(97+x))
    if N<0: break

print(''.join(ans[::-1]))

