#!/usr/bin/env python3
'''
A basic caching system
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A basic caching system
    '''
    def __init__(self):
        '''
        Construtor method
        '''
        super().__init__()

    def put(self, key, item):
        '''
        Assigns the item value to the key in the cache storage
        '''
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Returns the value of the key
        '''
        value = self.cache_data.get(key)
        return value
