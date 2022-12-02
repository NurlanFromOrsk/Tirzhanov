def print_hi(name):
    '''Принимая на вход объект name, печатает вместе с ним строку, добавляя name в конец
    Args:
        name (str or int or float): объект, который будет напечатан в конце строки
    '''
    print(f'Hi, {name}')

if __name__ == '__main__':
    '''Строка вернет True только в том случае, если программа будет запущена прямо.
    __main__ указывает на область видимости, где будет выполняться код.
    Если запустить Python-файл прямо, то значением __name__ будет __main__.
    Если же его запустить в качестве модуля, то значением будет уже не __main__, а название модуля
    '''
    print_hi('C#')