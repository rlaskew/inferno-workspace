import logging
import os 

from flask import Flask


application = Flask(__name__)

## https://realpython.com/python-command-line-arguments/
## PORT = sys.argv[1]

@application.route('/')
def hello():
    return 'Hello World!'


@application.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run('0.0.0.0',os.environ.get('PORT'),debug=True)
