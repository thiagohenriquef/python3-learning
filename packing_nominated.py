# **kwargs
def result_f1(**kwargs):
    for position, item in kwargs.items():
        print(f'{position} -> {item}')


def resultado(first, second, third):
    print(f'1 ) {first}')
    print(f'2 ) {second}')
    print(f'3 ) {third}')


if __name__ == '__main__':
    # result_f1(first="Thiago",
    #           second="Henrique",
    #           third="Ferreira")
    my_name = {
        'second': 'Henrique',
        'first': 'Thiago',
        'third': 'Ferreira'
    }
    resultado(**my_name)
