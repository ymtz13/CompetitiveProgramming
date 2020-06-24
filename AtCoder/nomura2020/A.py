H1, M1, H2, M2, K = map(int, input().split())
m1 = H1*60+M1
m2 = H2*60+M2
print(m2-K-m1)
