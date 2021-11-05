A, B = map(int, input().split())
EA = list(range(1, A+1))
EB = list(range(-1, -B-1, -1))

SA = sum(EA)
SB = sum(EB)
if A > B: EB[-1] -= SA + SB
if A < B: EA[-1] -= SA + SB

print(' '.join(map(str, EA + EB)))
