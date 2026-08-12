def logger(function):
    def apple(*args, **kwargs):
        print("Starting function...")
        result = function(*args, **kwargs)
        print("Function completed.")
        return result
    return apple
@logger
def add(a, b):
    return a + b
answer = add(4, 5)
print(answer)
import time


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        elapsed = end - start

        print(f"Execution time: {elapsed} seconds")

        return result

    return wrapper


@timer
def calculate():

    total = 0

    for i in range(1000000):
        total += i

    return total


print(calculate())