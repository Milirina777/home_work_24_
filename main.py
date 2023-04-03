import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from constants import DATA_DIR
from schema import RequestJsonSchema
from functions import get_query

app = Flask(__name__)


@app.post("/perform_query")
def perform_query():
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    try:
        data = RequestJsonSchema().load(request.json)
    except ValidationError:
        return f'Запрос неверен', 500

        values_cmd = ['sort', 'filter', 'limit', 'map', 'unique', 'regex']
        try:
            if data['cmd1'] not in values_cmd or data['cmd2'] not in values_cmd:
                raise ValidationError
        except ValidationError:
            return f'Название cmd-функции введено некорректно', 500

        with open(os.path.join(DATA_DIR, data['file_name'])) as result:
            result = get_query(data['cmd1'], data['value1'], result)
            result = get_query(data['cmd2'], data['value2'], result)

        return jsonify(result), 200


if __name__ == '__main__':
    app.run()
