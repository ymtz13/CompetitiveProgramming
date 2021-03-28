N = int(input())
A, B = map(int, input().split())
K = min(A, B) + 1

if A==B:
  ans = 'Aoki' if N%K==0 else 'Takahashi'

if A>B:
  ans = 'Takahashi'

if A<B:
  ans = 'Aoki' if A < N else 'Takahashi'

print(ans)
