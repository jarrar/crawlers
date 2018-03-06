"""
Pydoc

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
app.logger.info("                        'crwaler-db' app started.")
app.logger.info('=============================================================================')

# the 'db' import must come after instantiating Flask(__name__)
from models import db

from models import (HttpRecord)

from flask_restful import Api

# def populate_default_data():
#     casm = CasmData.CasmData()
#     casm.change_mode('single')


db.create_all()

#populate_default_data()

api = Api(app)

app.logger.info('APP REST API ready ...)')

# api.add_resource(Register, '/api/v1.0/register')
# api.add_resource(Cms, '/api/v1.0/cms/services')
# api.add_resource(HAStatus, '/api/v1.0/ha')
# api.add_resource(CasmMode, '/api/v1.0/mode')

if __name__ == '__main__':
    app.run(debug=True)
