A, B, C, D = [int(c) for c in input().split()]

p, q = max(C, D), min(C, D)
while q: p, q = q, p%q
E = C*D//p

Cmult_ge_A = A if A%C==0 else A+C-A%C
Dmult_ge_A = A if A%D==0 else A+D-A%D
Emult_ge_A = A if A%E==0 else A+E-A%E

nC = (B-Cmult_ge_A)//C+1
nD = (B-Dmult_ge_A)//D+1
nE = (B-Emult_ge_A)//E+1

print(B-A+1-nC-nD+nE)

