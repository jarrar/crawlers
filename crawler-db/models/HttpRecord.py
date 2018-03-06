"""
Put some pydoc
"""

import datetime
from . import db
from lib import Serializer


class HttpRecord(db.Model, Serializer):
    """

    A HttpRecord can only be registered once
    """

    id = db.Column(db.Integer, primary_key=True)  # pylint: disable=C0103
    url = db.Column(db.String())
    char_count = db.Column(db.Integer)

    def __init__(self, _url):
        self.url = _url

    def __repr__(self):
        return '<HttpRecord %r>' % self.url

    def __str__(self):
        return """<HttpRecord url={u} char_count={c}>""".format(u=self.url, c=self.char_count )
