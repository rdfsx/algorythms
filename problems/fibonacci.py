def fibonacci(n):
    def fibonacci_(n):
        if n <= 1:
            return n

        return fibonacci_(n - 1) + fibonacci_(n - 2)

    for i in range(n):
        print(fibonacci_(i))


print(fibonacci(10))
