A = int(input())
C = [n*n*n for n in range(1, A+1)]
print('YES' if A in C else 'NO')
