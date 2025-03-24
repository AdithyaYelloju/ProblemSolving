

def auditable(name=None):

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("In decorator")
            print(args)
            print(kwargs)
            print(name)
            response = func(*args, **kwargs)
            return response
        return wrapper
    return decorator

@auditable("name")
def main(name):
    print(f"{name=}")
    pass
    


@auditable("another")
def another():
    print("another")
    pass


main("adithya")
another()