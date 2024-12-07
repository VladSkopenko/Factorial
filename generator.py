def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


for value in factorial_generator(5):
    print(value)
