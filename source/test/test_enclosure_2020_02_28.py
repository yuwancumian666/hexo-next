import functools


def count1():
    fs = []
    for i in range(1, 4):
        def f():
            yield i*i
        fs.append(f)
    return fs


def count2():
    fs = []
    for i in range(1, 4):
        def f(m=i):
            return m*m
        fs.append(f)
    return fs


def log(mode):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print("[{}] log call: {}".format(mode, f.__name__))
            return f(*args, **kwargs)
        # wrapper.__name__ = f.__name__
        # wrapper.__doc__ = f.__doc__
        return wrapper
    return decorator


def LOG(f):
    def flog(*args, **kwargs):
        print("LOG call ", f.__name__)
        return f(*args)
    return flog


@log('Debug')
def func(x, y):
    print(x ** y)


if __name__ == "__main__":
    # f1, f2, f3 = count2()
    # print(f1())
    # print(f2())
    # print(f3())
    func(2, 3)
    print(func.__name__)

