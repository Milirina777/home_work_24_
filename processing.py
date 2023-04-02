from flask import abort
from typing import List, Union

from functions import mapping, limited_, filter_, unique_, sorted_, regex_


def filter_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'filter' and cmd2 == 'map':
            data = filter_(str_=value1)
            return mapping(colomn_=value2, data=data)
        elif cmd1 == 'filter' and cmd2 == 'limit':
            data = filter_(str_=value1)
            return limited_(value=value2, data=data)
        elif cmd1 == 'filter' and cmd2 == 'unique':
            data = filter_(str_=value1)
            return unique_(data=data)
        elif cmd1 == 'filter' and cmd2 == 'sort':
            data = filter_(str_=value1)
            return sorted_(data=data, asc=value2)
    except Exception as e:
        abort(400, e)


def map_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'map' and cmd2 == 'unique':
            data = mapping(colomn_=value1)
            return unique_(data=data)
        elif cmd1 == 'map' and cmd2 == 'limit':
            data = mapping(colomn_=value1)
            return limited_(value=value2, data=data)
        elif cmd1 == 'map' and cmd2 == 'filter':
            data = mapping(colomn_=value1)
            return filter_(str_=value2, data=data)
        elif cmd1 == 'map' and cmd2 == 'sort':
            data = mapping(colomn_=value1)
            return sorted_(data=data, asc=value2)
    except Exception as e:
        abort(400, e)


def sort_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'sort' and cmd2 == 'limit':
            data = sorted_(asc=value1)
            return limited_(value=value2, data=data)
        elif cmd1 == 'sort' and cmd2 == 'filter':
            data = sorted_(asc=value1)
            return filter_(str_=value2, data=data)
        elif cmd1 == 'sort' and cmd2 == 'unique':
            data = sorted_(asc=value1)
            return unique_(data=data)
        elif cmd1 == 'sort' and cmd2 == 'map':
            data = sorted_(asc=value1)
            return mapping(colomn_=value2, data=data)
    except Exception as e:
        abort(400, e)


def limit_in_cmd1(cmd1, cmd2, value1, value2):
    try:
        if cmd1 == 'limit' and cmd2 == 'map':
            data = limited_(value=value1)
            return mapping(colomn_=value2, data=data)
        elif cmd1 == 'limit' and cmd2 == 'filter':
            data = limited_(value=value1)
            return filter_(str_=value2, data=data)
        elif cmd1 == 'limit' and cmd2 == 'sort':
            data = limited_(value=value1)
            return sorted_(data=data, asc=value2)
        elif cmd1 == 'limit' and cmd2 == 'unique':
            data = limited_(value=value1)
            return unique_(data=data)
    except Exception as e:
        abort(400, e)

def regex_in_cmd1(cmd2: str, value1: str, value2: Union[int, str]):
    try:
        data: List[str] = regex_(reg=value1)
        if cmd2 == 'map':
            return mapping(colomn_=value2, data=data)
        elif cmd2 == 'filter':
            return filter_(str_=value2, data=data)
        elif cmd2 == 'sort':
            return sorted_(data=data, asc=value2)
        elif cmd2 == 'unique':
            return unique_(data=data)
        elif cmd2 == 'limit':
            return limited_(value=value2, data=data)
        abort(400)
    except Exception as e:
        abort(400, e)
