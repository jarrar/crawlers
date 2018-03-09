# A collection of all the routes that this application will expose.

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import requests
from app import app_obj

Interfaces = {
    "Db-REST": "http://crawler-db.docker:5050/api/v1.0/http_record",
    "Web-REST": "http://crawler-web.docker:5080/api/v1.0/http_request",
}

class CrawalForm(Form):
    """A Basic Form for getting the user Input and displaying the existing data."""
    url = TextField('Url:', validators=[validators.required()])

app_obj.config['SECRET_KEY'] = 'CurlyPython'

def get_crawl_data():
    """A function to get crawl data off of the crwal-db micro service.
    """
    db_rest_url = Interfaces['Db-REST']
    response = requests.get(url=db_rest_url)
    data = response.json()

    return data

def post_crawl_data(url):
    """A function that can be called to POST a new record. """
    web_rest_url = Interfaces['Web-REST']
    db_rest_url = Interfaces['Db-REST']

    # Request will go to crawaler-web REST api and get the info on char count of the url.
    response = requests.get(url=web_rest_url, params = {'url': url})
    response.raise_for_status()

    data = response.json()
    data_dict = json.loads(data)

    print("[-> crawler-web] status_code: %s" % response.status_code)
    print("[-> crawler-web] data %s" % data)
    print("[-> crawler-web] data_dict %s" % data_dict)


    print("[-> crawler-web] chars_num %s" % data_dict['char_count'])

    count = data_dict.get('char_count')
    data_param = {"url": url, "chars_num": count}
    print("[<- crawler-db] sending data_param %s" % data_param)

    response = requests.put(db_rest_url, data=data_param)
    print("[<- crawler-db] done doing a PUT")

    response.raise_for_status()
    data = response.json()
    print("[-> crawler-db] PUT result %s" % data)

@app_obj.route("/", methods=['GET', 'POST'])
@app_obj.route("/index", methods=['GET', 'POST'])
def display_form():
    form = CrawalForm(request.form)

    print form.errors
    if request.method == 'POST':
        url = request.form['url']

        if form.validate():
            # Save the comment here.
            #flash('URL passed: ' + url)
            post_crawl_data(url)
        else:
            flash('All the form fields are required. ')

    data = get_crawl_data()
    return render_template('form.html', form=form, data=data)
