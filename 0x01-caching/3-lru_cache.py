#!/usr/bin/env python3
'''
A basic implementation of a LRU caching system
'''


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    A LRU caching algorithm
    '''

    def __init__(self):
        '''
        Constructor method
        '''
        super().__init__()
        self.lruTracker = {}

    def addToLRUTracker(self, key):
        '''
        Adds a new key to the LRUTracker dict
        '''
        mruNo = max(self.lruTracker.values())
        self.lruTracker[key] = mruNo + 1

    def put(self, key, item):
        '''
        Update or add items to cache_data
        '''
        if key is None or item is None:
            pass
        else:
            if self.get(key) is None:
                if len(self.cache_data) == self.MAX_ITEMS:
                    keyToDiscard = sorted(self.lruTracker,
                                          key=lambda key: self.lruTracker[key],
                                          reverse=True)[-1]
                    print("DISCARD:", keyToDiscard)
                    # Remove data from cache
                    self.cache_data.pop(keyToDiscard)
                    # Add new data to cache
                    self.cache_data.update({key: item})
                    # Add new data to LRUTracker
                    self.addToLRUTracker(key)
                    # Remove data from LRU Tracker
                    self.lruTracker.pop(keyToDiscard)
                else:
                    self.cache_data.update({key: item})
                    if len(self.lruTracker) == 0:
                        self.lruTracker[key] = 1
                    else:
                        self.addToLRUTracker(key)
            else:
                self.cache_data.update({key: item})

    def get(self, key):
        '''
        Returns the Value of a Key in the cache_data
        '''
        value = self.cache_data.get(key)

        if value:
            keyPriorityNo = self.lruTracker.get(key)
            mruNo = max(self.lruTracker.values())
            if keyPriorityNo < mruNo:
                self.lruTracker[key] = mruNo + 1

        return value
