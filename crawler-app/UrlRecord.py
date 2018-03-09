# -*- coding: UTF-8 -*-
"""
"""

import json

from flask import request
from flask_restful import Resource
import requests


class UrlRecord(Resource):
    """ A REST API to interact with the URL record DB Table.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    #                                        HTTP methods.
    # ---------------------------------------------------------------------------------------------

    @classmethod
    def get(cls):
        """Implements http GET method.

        Input format:

            - Gets all records
            - Gets a particular record
        """
        url = request.args.get('url')
        if not url:
            return None

        full_url = url

        if not url.startswith('http://') and not url.startswith('https://'):
            full_url = 'http://' + url

        r = requests.get(full_url)

        print(r.status_code)
        print(r.headers["content-type"])
        print(len(r.text))

    @classmethod
    def post(cls):
        raise NotImplementedError("POST method is not supported.")

    @classmethod
    def put(cls):
        """
        Input format:
            - data: JSON
            {
                "url": "",
                "number_chars": 0,
            }
        :return:
        """
        data = request.args.get('data')
        if not url:
            return None

        print("Data: %s", data)

    @classmethod
    def delete(cls):
        raise NotImplementedError("DELETE method is not supported.")
