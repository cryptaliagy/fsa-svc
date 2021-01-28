from flask import (
    Flask,
    request,
    make_response,
    jsonify,
    send_file
)
from flask_json_schema import JsonSchema

from fsa_svc.lib import csv_string_to_dicts
import pyfsa.lib.csv_convert as csv
import pyfsa.lib.fsa as fsa
import os

from datetime import datetime

import logging

app = Flask(__name__)
schema = JsonSchema(app)

logging.basicConfig(
    format=f"[%(asctime)s] [{os.getpid()}] [%(levelname)s] - %(name)s - %(message)s",
    level=logging.DEBUG,
    datefmt='%Y/%m/%d %H:%M:%S %z')


@app.route('/', methods=['POST'])
@schema.validate({
    'properties': {
        'transitions': {
            'type': 'string'
        },
        'start': {
            'type': 'string'
        },
        'end': {
            'type': 'string',
        },
        'engine': {
            'type': 'string',
        },
    },
    'required': ['transitions']
})
def render_graph():
    data = request.get_json()

    logging.debug(data)
    logging.debug(type(data))
    data['transitions'] = csv_string_to_dicts(data['transitions'])
    data['transitions'] = csv.rows_to_transitions(data['transitions'])

    file_name = str(datetime.now()) + '.png'

    try:
        fsa.get_state_graph(
            **data,
            name=file_name
        )
    except Exception:
        breakpoint()
        resp = jsonify({'error': 'fsa failed to create graph'})
        return make_response(resp, 400)

    return send_file(f'../../{file_name}', 'image/png')


if __name__ == '__main__':
    app.run()
