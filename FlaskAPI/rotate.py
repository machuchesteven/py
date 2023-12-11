import logging
from flask import Flask, request, jsonify
from logging.handlers import RotatingFileHandler
import requests
from major import index

app = Flask(__name__)


handler = RotatingFileHandler(
        'app.log',
        maxBytes=1024 * 1024)
handler.setLevel(logging.INFO)

app.logger.addHandler(handler)

app.logger.info('This message goes to stderr and app.log!')
logging.basicConfig(filename='app.log', level=logging.INFO)

app.add_url_rule('/', 'index', index,methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)