def f1():
    print('This is f1 function')
    print(__name__)


def f2():
    print('This is f2 function')
    print(__name__)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


if __name__ == '__main__':
    f1()
    f2()
    print(add(10, 20))
    print(sub(30, 10))
