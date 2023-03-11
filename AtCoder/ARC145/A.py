N = int(input())
S = input()


def solve(N, S):
  if N <= 1:
    return True

  if N == 2:
    return len(set(S)) == 1

  if S[0] == 'B':
    return True

  if S[-1] == 'B':
    return False

  return S != 'ABAA'


print('Yes' if solve(N, S) else 'No')
