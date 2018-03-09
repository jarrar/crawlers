# -*- coding: UTF-8 -*-
"""
A class that acts as a resource for the REST
"""

import json

from flask import request
from flask_restful import Resource
from models.HttpRecord import HttpRecord


class DatabaseApi(Resource):
    """A class that provides REST implementation for the registration process with the CASM."""

    def __init__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    #                                        HTTP methods.
    # ---------------------------------------------------------------------------------------------

    @classmethod
    def get(cls):
        """Implements http GET method."""
        url = request.args.get('url')
        return_data = list()

        if not url:
            # it indicates that it needs to access all records
            all_data = HttpRecord.get_all_records()

            for datum in all_data:
                entry = dict()
                entry['url'] = datum.url
                entry['chars_count'] = datum.char_count

                print("url: ", datum.url)
                print("count: ", datum.char_count)

                return_data.append(entry)

            # return [{"url": "jarrar.com", "chars_count": 23}]
            return return_data

        print("GET")
        response = dict()
        return json.dumps(response)

    @classmethod
    def put(cls):
        """A method to terminate the 'PUT' http verb, using PUT as it will be adding a new record
        each time.
        """
        print("[crawler-web] Received http verb: %s" % request.method)
        url = request.form['url']
        num = request.form['chars_num']

        print("Storing: %s, %s" % (url, num))

        db_record = HttpRecord(url, num)
        db_record.add_record()

        return {"status": "Success"}

    @classmethod
    def post(cls):
        raise NotImplementedError("POST method is not supported.")

    @classmethod
    def delete(cls):
        raise NotImplementedError("DELETE method is not supported.")
