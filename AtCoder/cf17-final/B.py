S = input()
N = [S.count(c) for c in 'abc']
print('YES' if max(N)-min(N)<=1 else 'NO')