#!/usr/bin/python3
""" MRU caching """
from django.dispatch import receiver
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class inheriting from BaseCaching """
    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.store = {}
        self.recent = 0

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item
            self.store[key] = self.recent
            self.recent += 1
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent = 0
            # store key in temp to prevent removal
            temp = key
            # find the key with the highest recent value
            for ky in self.store:
                rec = self.store.get(ky)
                if rec > recent and ky != temp:
                    recent = rec
                    key = ky
            print("DISCARD: {}".format(key))
            # remove the key from cache and store
            self.cache_data.pop(key)
            self.store.pop(key)

    def get(self, key):
        """ Return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        self.store[key] = self.recent
        self.recent += 1
        return self.cache_data.get(key)
