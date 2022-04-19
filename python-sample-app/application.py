import logging

from flask import Flask


application = Flask(__name__)


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
    application.run('localhost',5000,debug=True)
