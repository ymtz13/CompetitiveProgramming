from sys import stderr

Fib = ['b', 'a']
for i in range(20):
  Fib.append(Fib[-1] + Fib[-2])

print(Fib[-1])
print(len(Fib[-1]), file=stderr)