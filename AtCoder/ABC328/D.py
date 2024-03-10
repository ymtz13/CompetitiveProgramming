S = input()

stack = [""] * (len(S) + 10)
n = 2

ABC = ["A", "B", "C"]

for c in S:
    stack[n] = c
    n += 1

    if stack[n - 3 : n] == ABC:
        stack[n - 3] = stack[n - 2] = stack[n - 1] = ""
        n -= 3


print("".join(stack))
