def gen_fib():
    a = 0
    b = 1
    while(True):
        yield a
        a, b = b, a+b


generator = gen_fib()
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
