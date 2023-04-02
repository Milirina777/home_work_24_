import os

from flask import Flask, request, Response, abort
from constants import DATA_DIR
from processing import filter_in_cmd1, map_in_cmd1, sort_in_cmd1, limit_in_cmd1, regex_in_cmd1

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query():
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    try:
        cmd1 = request.args['cmd1'] or request.json['cmd1']  # type: ignore
        value1 = request.args['value1'] or request.json['value1']  # type: ignore
        cmd2 = request.args['cmd2'] or request.json['cmd2']  # type: ignore
        value2 = request.args['value2'] or request.json['value2']  # type: ignore
        file_name = request.args['file_name'] or request.json['file_name']  # type: ignore
        log_file = os.path.join(DATA_DIR, file_name)
        if not os.path.isfile(log_file):
            abort(400, 'Ошибка. Имя имя файла не несоответствует')
        elif cmd1 == 'filter':
            return Response(filter_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'map':
            return Response(map_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'sort':
            return Response(sort_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'limit':
            return Response(limit_in_cmd1(cmd2, value1, value2))
        elif cmd1 == 'regex':
            return Response(regex_in_cmd1(cmd2, value1, value2))
        else:
            abort(400, 'Введенные данные недопустимы')
    except Exception as e:
        abort(400, e)
    return app.response_class('', content_type="text/plain")

if __name__ == '__main__':
    app.run()