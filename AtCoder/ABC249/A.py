A, B, C, D, E, F, X = map(int, input().split())

L1 = (X // (A + C) * A + min(X % (A + C), A)) * B
L2 = (X // (D + F) * D + min(X % (D + F), D)) * E

print('Takahashi' if L1 > L2 else 'Aoki' if L1 < L2 else 'Draw')
