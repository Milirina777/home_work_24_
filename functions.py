from constants import LOG_DIR
import re

def data_():
    """Формирует массив с данными"""
    with open(LOG_DIR) as f:
        data = map(lambda v: v.strip(), f)
        return list(data)


def mapping(colomn_: str, data: list[str]):
    """Возвращает по номеру колонки требуемую колонку из массива"""
    if data is None:
        data = data_()
    colomn_ = int(colomn_)

    return list(map(lambda row: row.split(' ')[colomn_], data))


def filter_(str_: str, data: list[str]):
    """Возвращает строки по вводимому значению с этим значением"""
    if data is None:
        data = data_()

    return list(filter(lambda row: row if str_ in row else None, data))


def unique_(parametr_, data: list[str]):
    """Возвращает массив с уникальными значениями"""
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result


def sorted_(asc: str, data: list[str]):
    """Сортирует массив"""
    if data is None:
        data = data_()
    if asc == 'asc':
        res = True
    else:
        res = False
    return sorted(data, reverse=res)


def limited_(value: str, data: list[str]):
    """Лимитирует вывод данных с массива"""
    if data is None:
        data = data_()

    value = int(value)
    counter = 0
    result = []
    while counter < value:
        for i in data:
            result.append(i)
            counter += 1
            if counter == value:
                break

    return result


FILE_NAME = './apache_logs.txt'


def regex_(reg: str, data: list[str]):
    """Возвращает строки со значениями массива"""
    if data is None:
        data = data_()
    if 'png' in reg:
        regex_reg = 'images\/\S*\.png'
    else:
        raise ValueError

    regex = re.compile(regex_reg)
    result = []
    for line in data:
        item = regex.findall(line)
        if item:
            result.append(line)
    return result


def get_query(cmd: str, parametr_, data=None):
    if cmd == 'filter':
        return filter_(parametr_=parametr_, data=data)
    elif cmd == 'limit':
        return limited_(parametr_=parametr_, data=data)
    elif cmd == 'map':
        return mapping(parametr_=parametr_, data=data)
    elif cmd == 'sort':
        return sorted_(parametr_=parametr_, data=data)
    elif cmd == 'unique':
        return unique_(parametr_=parametr_, data=data)
    elif cmd == "regex":
        try:
            return regex_(parametr_=parametr_, data=data)
        except ValueError as e:
            print('Ошибка параметра regex')
