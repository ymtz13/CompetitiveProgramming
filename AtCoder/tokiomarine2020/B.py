A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
D = abs(A-B)
X = V-W
print("YES" if D<=X*T else "NO")
