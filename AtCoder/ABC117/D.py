N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
D = 100

v0 = []
vm = []
vk = []
for i in range(D):
    n1 = 0
    for a in A:
        if a>>i &1: n1+=1
    v0.append(n1 * 2**i)
    vm.append(max(n1,N-n1) * 2**i)
    vk.append((N-n1) * 2**i if K>>i &1 else n1 * 2**i)

for a in A:
    print('{:05b}'.format(a))
print(v0)
print(vm)
print(vk)

m = sum(vk)
for i in range(D):
    if K>>i &1: m = max(m, sum(vk[i+1:]) + v0[i] + sum(vm[:i]))

print(m)

# 1001100101
# >=
# 1001100101
# 1001100100
# 10011000XX
# 10010XXXXX
# 1000XXXXXX
# 0XXXXXXXXX

# 001
# 110
# 011
