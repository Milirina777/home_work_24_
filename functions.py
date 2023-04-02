from constants import LOG_DIR
from typing import List, Iterable, Union, Any
import re


def mapping(colomn_: Any, data: Iterable[str] = None):
    """Возвращает по номеру колонки требуемую колонку из массива"""
    if data is None:
        data = data_()
    colomn_ = int(colomn_)

    return list(map(lambda row: row.split(' ')[colomn_], data))


def filter_(str_: Any, data: Iterable[str] = None):
    """Возвращает строки по вводимому значению с этим значением"""
    if data is None:
        data = data_()

    return list(filter(lambda row: row if str_ in row else None, data))


def unique_(data: Iterable[str]):
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


def sorted_(asc: Any, data: Iterable[str] = None):
    """Сортирует массив"""
    if data is None:
        data = data_()
    if asc == 'asc':
        return sorted(data)
    elif asc == 'desc':
        return sorted(data, reverse=True)


def limited_(value: Any, data: Iterable[str] = None):
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


def data_():
    """Формирует массив с данными"""
    with open(LOG_DIR) as f:
        data = map(lambda v: v.strip(), f)
        return list(data)

def regex_(reg: Union[str, int], data: Iterable[str] = None):
    """Возвращает строки со значениями массива"""
    if data is None:
        data = data_()
    regex = re.compile(fr"{reg}")
    result: List[str] = [i for i in data if regex.search(i)]
    return result
