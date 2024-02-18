def welcome() -> None:
    print("welcome")


def welcome_python(name: str, hope: str = '你好呀') -> None:
    print(f'你好{name}')
    print(f'\t{hope}')


if __name__ == '__main__':
    print("hello")
    welcome()
    welcome_python('K君')
    welcome_python('Kirito', '希望你能过初会')
