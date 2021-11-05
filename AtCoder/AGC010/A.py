N = int(input())
A = list(map(int, input().split()))
print('YES' if len([a for a in A if a % 2 == 1]) % 2 == 0 else 'NO')
