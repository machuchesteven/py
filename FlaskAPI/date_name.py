import os
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from datetime import datetime

app = Flask(__name__)
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
def get_log_filename():
    return os.path.join(log_dir, f"log{datetime.now().strftime('%Y%m%d')}.log")
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
log_file = get_log_filename()

file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)  # Set the desired log level

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)  # Set the desired log level for the app logger

# Example route using the logger
@app.route('/')
def index():
    app.logger.info('This is an info log message')
    app.logger.error('This is an error log message')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
