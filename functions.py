import re


def mapping(str_: str, data: list[str]) -> list:
    """Возвращает по номеру колонки требуемую колонку из массива"""
    coloum_ = int(str_)
    if coloum_ == 0:
        result = list(map(lambda x: x.split()[coloum_], data))
    elif coloum_ == 1:
        result = list(map(lambda x: x.split()[3] + x.split()[4], data))
    elif coloum_ == 2:
        result = list(map(lambda x: " ".join(x.split()[5:]), data))

    return result


def filter_(str_: str, data: list[str]) -> list:
    """Возвращает строки по вводимому значению с этим значением"""
    return list(filter(lambda x: str_ in x, data))


def unique_(str_: str, data: list[str]) -> list:
    """Возвращает массив с уникальными значениями"""
    return list(set(data))


def sorted_(str_: str, data: list[str]) -> list:
    """Сортирует массив"""
    reverse = (str_ == 'desc')
    return sorted(data, reverse=reverse)


def limited_(str_: str, data: list[str]) -> list:
    """Лимитирует вывод данных с массива"""
    return data[: int(str_)]

def regex_(str_: str, data: list[str]) -> list:
    """Возвращает строки со значениями массива"""
    regex = re.compile(str_)
    return list(filter(lambda v: re.search(regex, v), data))


def get_query(cmd: str, str_: str, data: list[str]) -> list:
    if cmd == 'filter':
        return filter_(str_=str_, data=data)
    elif cmd == 'limit':
        return limited_(str_=str_, data=data)
    elif cmd == 'map':
        return mapping(str_=str_, data=data)
    elif cmd == 'sort':
        return sorted_(str_=str_, data=data)
    elif cmd == 'unique':
        return unique_(str_=str_, data=data)
    elif cmd == "regex":
        try:
            return regex_(str_=str_, data=data)
        except ValueError as e:
            print('Ошибка параметра regex')
