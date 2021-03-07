N = int(input())
t = sorted(list('indeednow'))
for _ in range(N): print('YES' if sorted(list(input())) == t else 'NO')