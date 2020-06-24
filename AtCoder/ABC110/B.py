N, M, X, Y = list(map(int, input().split()))
x = max(list(map(int, input().split())))
y = min(list(map(int, input().split())))

print('No War' if max(x,X)<min(y,Y) else 'War')
