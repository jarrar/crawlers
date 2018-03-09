# -*- coding: UTF-8 -*-
"""
A class that acts as a resource for the REST request for GET.
"""

import json

from flask import request
from flask_restful import Resource
import requests


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
    url = request.args.get('url')
    if not url:
        print("No Url was provided, returning.")
        return None

    full_url = url

    if not url.startswith('http://') and not url.startswith('https://'):
        full_url = 'http://' + url

    print("Making request: %s", full_url)
    r = requests.get(full_url)

    r.raise_for_status()

    response = dict()
    response['status_code'] = r.status_code
    response['char_count'] = len(r.text)

    print("Response: %s", response)

    return json.dumps(response)

  @classmethod
  def post(cls):
    raise NotImplementedError("POST method is not supported.")

  @classmethod
  def put(cls):
    raise NotImplementedError("PUT method is not supported.")

  @classmethod
  def delete(cls):
    raise NotImplementedError("DELETE method is not supported.")
