"""
An app that is an entry point for the crawler-web which is meant to receive a url and then
execute URL request.
"""
from flask import Flask
import logging
from logging import Formatter, FileHandler
from HttpRequest import HttpRequest

# the name app is also imported in models/__init__.py,
app = Flask(__name__)

app.logger.propagate = False

app.debug = True

file_handler = FileHandler('/var/log/app.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
                                    '[in %(pathname)s:%(lineno)d]'))

app.logger.addHandler(file_handler)

app.logger.info('=============================================================================')
app.logger.info("                        'crwaler-web' app started.")
app.logger.info('=============================================================================')

from flask_restful import Api

api = Api(app)

app.logger.info('WEB-APP REST API ready ...)')
api.add_resource(HttpRequest, '/api/v1.0/http_request')

if __name__ == '__main__':
    app.run(debug=True)