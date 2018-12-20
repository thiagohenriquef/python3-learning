def all_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    all_params('Thiago', 'Henrique', 'Ferreira')
    all_params('Thiago', 'Henrique', 'Ferreira',
               first='Thiago', second='Henrique', third='Ferreira')
