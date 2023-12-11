# API with logging functionality in deployment mode

from flask import Flask, request, jsonify, has_request_context
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler
# file_handler = RotatingFileHandler('flask.log', maxBytes=1024 * 1024 * 10, backupCount=20)
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)
    
formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)

app = Flask(__name__)


logging.basicConfig(filename='app.log', level=logging.INFO)
default_handler.setFormatter(formatter)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return jsonify({'message': 'POST method'})
    else:
        name = request.args.get('name')
        logging.info('name: %s', name)
        logging.error('name: %s', name)
        return jsonify({'message': 'GET method'})





if __name__ == '__main__':
    app.run(debug=True,)
