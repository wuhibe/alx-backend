#!/usr/bin/python3
""" task 0 """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' dictionary caching system '''
    def __init__(self):
        ''' Initialize class '''
        super().__init__()

    def put(self, key, item):
        ''' method to add to the dictionary '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' getter method '''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
