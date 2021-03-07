N, X = map(int, input().split())
A = list(map(int, input().split()))
print(' '.join(map(str, [v for v in A if v != X])))
