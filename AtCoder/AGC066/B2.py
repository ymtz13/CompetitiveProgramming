def f(X):
    return sum(map(int, str(X)))


# print(f(331))
# print(f(2024))
# print(f(1))
input()


x = 10**99
d0 = f(x)
X = []
for i in range(100):
    d = f(x)
    # print(f"{i: 4d} {d: 4d} {x}")
    X.append(x)
    x = x // 2

    # if d != d0:
    #     break

# print(X[50:])

ans = []
for x in X[50:]:
    ans.append(f"{x:0100d}")

# for a in ans:
#     print(a)

ans = int("".join(ans))
# print(len(str(ans)))
print(ans)

x = ans
for i in range(55):
    d = f(x)
    # print(f"{i: 4d} {d: 4d} {x}")
    # print(f"{i: 4d} {d: 4d}")
    x = x * 2
