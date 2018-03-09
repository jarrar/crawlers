'''This module is for the casm related libraries.
'''
from sqlalchemy.inspection import inspect

class Serializer(object):
    '''A class to serialize a DB object into JSON. '''
    def serialize(self):
        '''To serialize a class.'''
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
