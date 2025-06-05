def fibonacci(number: int):
    if number <= 1:
        return number
    fib1, fib2 = 0, 1
    while number > 1:
        fib1, fib2 = fib2, fib1 + fib2
        number-=1
    return fib2

print(fibonacci(5))


