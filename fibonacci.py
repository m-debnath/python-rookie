def fib(n):
    """Prints a series of fibonacci numbers up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    # print()
    
fib(2000)
    