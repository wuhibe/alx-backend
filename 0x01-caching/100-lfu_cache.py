#!/usr/bin/python3
""" LFU caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inheriting from BaseCaching """
    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.store = {}
        self.recent = 0
        self.lst = []

    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item
            self.store[key] = self.recent
            self.recent += 1
            self.lst.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = []
            least = self.recent
            val = self.recent
            for x in self.store:
                if self.lst.count(x) < least:
                    keys.clear()
                    least = self.lst.count(x)
                    keys.append(x)
                elif self.lst.count(x) == least:
                    keys.append(x)
            for x in keys:
                vl = self.store[x]
                if vl < val:
                    val = vl
                    key = x
            print("DISCARD: {}".format(key))
            self.cache_data.pop(key)
            self.store.pop(key)

    def get(self, key):
        """ Return the value linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        self.store[key] = self.recent
        self.recent += 1
        self.lst.append(key)
        return self.cache_data.get(key)
