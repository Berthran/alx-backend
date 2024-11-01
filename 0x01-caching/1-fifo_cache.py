#!/usr/bin/env python3
'''
A basic implementation of a FIFO caching system
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    A FIFO caching algorithm
    '''

    def __init__(self):
        '''
        Constructor method
        '''
        super().__init__()

    def put(self, key, item):
        '''
        Update or add items to cache_data
        '''
        if key is None or item is None:
            pass
        else:
            if self.get(key) is None:
                if len(self.cache_data) == self.MAX_ITEMS:
                    keysReversed = sorted(self.cache_data.keys(), reverse=True)
                    keyToDiscard = keysReversed[-1]
                    print("DISCARD:", keyToDiscard)
                    self.cache_data.pop(keyToDiscard)
                    self.cache_data.update({key: item})
                else:
                    self.cache_data.update({key: item})
            else:
                self.cache_data.update({key: item})

    def get(self, key):
        '''
        Returns the Value of a Key in the cache_data
        '''
        return self.cache_data.get(key)
