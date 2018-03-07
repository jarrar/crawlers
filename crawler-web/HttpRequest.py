# -*- coding: UTF-8 -*-
"""
A class that acts as a resource for the REST request for GET.
"""

import json

from flask import request
from flask_restful import Resource


class HttpRequest(Resource):
    """A class that provides REST implementation for the registration process with the CASM."""

    def __init__(self):
        pass

    # ---------------------------------------------------------------------------------------------
    #                                        HTTP methods.
    # ---------------------------------------------------------------------------------------------

    @classmethod
    def get(cls):
        """Implements http GET method."""
        data_type = request.args.get('data_type')
        if not data_type:
            data_type = 'registration'

        print('JARRAR')
        # if data_type == 'registration':
        #     scripts_data = Script.get_registered_scripts()
        #     print('scripts_data: %s' % scripts_data)
        #     return json.dumps([s.serialize() for s in scripts_data])
        #
        # if data_type == 'no_switch_requests':
        #     scripts_data = Script.get_scripts_without_switch()
        #     print 'scripts_data: %s' % scripts_data
        #     return json.dumps([s.serialize() for s in scripts_data])

    @classmethod
    def post(cls):
        raise NotImplementedError("POST method is not supported.")

    @classmethod
    def put(cls):
        raise NotImplementedError("PUT method is not supported.")

    @classmethod
    def delete(cls):
        raise NotImplementedError("DELETE method is not supported.")
