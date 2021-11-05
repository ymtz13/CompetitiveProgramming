N = int(input())
S = input()
for i, c in enumerate(S):
  if c=='1':
    print('Takahashi' if i%2==0 else 'Aoki')
    exit()
