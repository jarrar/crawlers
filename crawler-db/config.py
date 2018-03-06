"""
This module defines basic configurations for the SQL Alchemy.
"""

import os
# basedir = os.path.abspath(os.path.dirname(__file__))
base_dir = '/var/log/db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'crawler.db')