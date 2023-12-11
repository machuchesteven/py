from flask import request, jsonify
import requests
import logging

def index():
    if request.method == 'POST':
        logging.info(request.get_json())
        return jsonify({'message': 'POST method'})
    else:
        name = request.args.get('name')
        if name is None:
            logging.info('No name specified')
            try:
                response = requests.post('http://localhost:5000/', json={'name': 'Kiko'})
                logging.info(response.json())
            except Exception as e:
                logging.error(e)
        else:
            logging.info('name: %s', name)
    return jsonify({'message': 'GET method'})