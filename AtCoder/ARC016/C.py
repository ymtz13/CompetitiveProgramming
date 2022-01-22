N, M = map(int, input().split())
C = []
P = []
for _ in range(M):
  c, cost = map(int, input().split())
  C.append(cost)

  prob = [0] * N
  for _ in range(c):
    idol, p = map(int, input().split())
    prob[idol - 1] = p
  P.append(prob)

E = [0]
for B in range(1, (1 << N)):
  e = []
  for cost, prob in zip(C, P):
    prob_success = 0
    exp = 0
    for i, p in enumerate(prob):
      b = 1 << i
      if B & b:
        prob_success += p
        exp += E[B - b] * p

    if prob_success == 0: continue

    exp /= prob_success
    e.append(exp + cost / prob_success * 100)

  E.append(min(e))

print(E[-1])

# p + 2*(1-p)*p + 3*(1-p)^2 * p
# = p * S(1-p)
# = 1/p

#      S(q) = 1 + 2*q + 3*q^2 + ...
#     qS(q) =     1*q + 2*q^2 + ...
# (1-q)S(q) = 1 +   q +   q^2 + ...
#           = 1 / (1-q)

# S(1-p) = 1/(1-(1-p))^2 = 1/p^2
