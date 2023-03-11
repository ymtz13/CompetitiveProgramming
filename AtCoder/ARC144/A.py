N = int(input())
x = [N % 4] + [4] * (N // 4)
if x[0] == 0: x = x[1:]

print(N * 2)
print(''.join(map(str, x)))
