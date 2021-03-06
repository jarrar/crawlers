"""
This file defines all the models needed.
"""

import datetime
from . import db
from lib import Serializer


class HttpRecord(db.Model, Serializer):
    """
    A class that represents a Database record for url and number of chracters it returns.
    """

    id = db.Column(db.Integer, primary_key=True)  # pylint: disable=C0103
    url = db.Column(db.String())
    char_count = db.Column(db.Integer)

    def __init__(self, _url, _num):
        self.char_count = _num
        self.url = _url

    def __repr__(self):
        return '<HttpRecord %r>' % self.url

    def __str__(self):
        return """<HttpRecord url={u} char_count={c}>""".format(u=self.url, c=self.char_count)

    @classmethod
    def get_all_records(cls):
        all_records = cls.query.all()
        return all_records

    def add_record(self):
        """

        :return:
        """
        self.req_time = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S.%f")

        print("[crawler-db] insertin a row")
        db.session.add(self)
        db.session.commit()
