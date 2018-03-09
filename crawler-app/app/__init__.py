from flask import Flask

# Here it craetes a Flask app for the current module, passing __name__ is very critical here it
# indicates to the Flask that it should look for other resources that it needs to load like
# templates etc from this dir. That is why there is a dir templates/.

# PECULIARITIES:
# Note that the module is named app it is clearfrom the fact that the name of the dir is app and
# that it has __init__.py, it is reference in the 'from app ...'.
# however this module has a varaiable called app which is an instance of Flask() class and is a
# member of the module app.
#
# routes module ha sto be imported after app=Flask() becase routes will need to import the instance
# app.

app_obj = Flask(__name__)
from app import routes
