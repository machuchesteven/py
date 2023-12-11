import os
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask

app = Flask(__name__)

# Create a logs directory if it doesn't exist
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

log_file = os.path.join(log_dir, 'app.log')

file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)  # Set the desired log level

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    app.logger.info('This is an info log message')
    app.logger.error('This is an error log message')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()