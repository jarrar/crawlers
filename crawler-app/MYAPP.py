from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# from flask_wtf import Form
# from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
#
# from wtforms import validators, ValidationError


app = Flask(__name__)

from routes import basic_route


# @app.route("/")
# def index():
#     return "Flask App ---->"


# @app.route("/hello/<string:name>/")
# def hello(name):
#     return render_template(
#         'test.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
