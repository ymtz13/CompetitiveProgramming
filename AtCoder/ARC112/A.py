T = int(input())
for _ in range(T):
  L, R = map(int, input().split())
  K = max(0, R-2*L+1)  
  print(K*(K+1)//2)
