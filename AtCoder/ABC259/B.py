from math import cos, sin, tau

a, b, d = map(int, input().split())

P = a + b * 1j
R = cos(d * tau / 360) + sin(d * tau / 360) * 1j
Q = P * R

print(Q.real, Q.imag)
