def fib(seq=[0, 1]):
    seq.append(seq[-1] + seq[-2])
    return seq


def fib_2(seq=(0, 1)):
    return seq + (seq[-1] + seq[-2],)


def fib_3(seq=None):
    seq = seq or [0, 1]
    return seq.append(seq[-1] + seq[-2])


if __name__ == '__main__':
    print('-------------------- fib function --------------------------------')
    start = fib()
    print(start, id(start))
    print(fib(start))
    restart = fib()
    print(restart, id(restart))

    # a big problem with mutability using default arguments!!!
    # Solution => use tuples
    print('-------------------- fib_2 function --------------------------------')
    start = fib_2()
    print(start, id(start))
    print(fib_2(start))
    restart = fib_2()
    print(restart, id(restart))

    # Another solution using fib_3 function
    print('-------------------- fib_3 function --------------------------------')
    start = fib_3()
    print(start, id(start))
    print(fib_3(start))
    restart = fib_3()
    print(restart, id(restart))
