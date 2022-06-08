def decorator(fn):
    def wrapper(*args, **kwargs):
        print("Hi hi")
        fn(*args, **kwargs)
        print("Bye bye")

    return wrapper


@decorator
def square(x: int):
    return x ** 2


