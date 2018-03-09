"""
Pydoc.
"""
from flask import Flask
import logging
from logging import Formatter, FileHandler


# the name app is also imported in models/__init__.py,
app = Flask(__name__)

app.config.from_pyfile('config.py')

app.logger.propagate = False

app.debug = True

file_handler = FileHandler('/var/log/app.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
                                    '[in %(pathname)s:%(lineno)d]'))

app.logger.addHandler(file_handler)

app.logger.info('=============================================================================')
app.logger.info("                        app=crwaler-db started.")
app.logger.info('=============================================================================')

# the 'db' import must come after instantiating Flask(__name__)
from models import db
from models import HttpRecord

from flask_restful import Api
import DatabaseApi

db.create_all()

api = Api(app)

app.logger.info('[crawler-db] REST API ready APP :)')

# curl -X PUT "${DB_URL}?url=cnn.com&chars_num=2"
api.add_resource(DatabaseApi.DatabaseApi, '/api/v1.0/http_record')

if __name__ == '__main__':
    app.run(debug=True)
