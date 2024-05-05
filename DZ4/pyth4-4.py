def call_info_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами: {args} и именованными аргументами: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@call_info_decorator
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

