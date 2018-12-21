def log(function):
    def decorator(*args, **kwargs):
        print(f'Calling this function: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        result = function(*args, **kwargs)
        print(f'result => {result}')
        return result
    return decorator


@log
def sum(a, b):
    return a + b


@log
def sub(a, b):
    return a - b 


if __name__ == '__main__':
    print(sum(b=3, a=2))
    print(sub(b=3, a=2))
