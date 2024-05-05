def fibonacci_generator(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
n = 10
fibonacci_gen = fibonacci_generator(n)

for num in fibonacci_gen:
    print(num)

