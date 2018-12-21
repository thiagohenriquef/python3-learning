from app.util.generator import new_name
from app.business import name_exist
from app.business.backend import add_nome


def main():
    while True:
        nome = new_name()
        if not name_exist():
            add_nome()
            break
    print(f'Created new test name: "{nome}"')


if __name__ == '__main__':
    main()
