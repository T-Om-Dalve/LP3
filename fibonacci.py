# Iterative Fibonacci (simplified)

def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

n = int(input("Enter n(Iterative): "))
print(f"Fibonacci({n}) = {fib_iterative(n)}")

# Recursive Fibonacci

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

n = int(input("Enter n(Recursive): "))
print(f"Fibonacci({n}) = {fib_recursive(n)}")