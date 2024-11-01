#!/usr/bin/env python3
'''
A basic implementation of a MRU caching system
'''


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    A MRU caching algorithm
    '''

    def __init__(self):
        '''
        Constructor method
        '''
        super().__init__()
        self.mruTracker = {}

    def addToMruTracker(self, key):
        '''
        Adds a new key to the mruTracker dict
        '''
        mruNo = max(self.mruTracker.values())
        self.mruTracker[key] = mruNo + 1

    def put(self, key, item):
        '''
        Update or add items to cache_data
        '''
        if key is None or item is None:
            pass
        else:
            if self.get(key) is None:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    keyToDiscard = sorted(self.mruTracker,
                                          key=lambda key: self.mruTracker[key],
                                          reverse=False)[-1]
                    print("DISCARD:", keyToDiscard)
                    # Remove data from cache
                    self.cache_data.pop(keyToDiscard)
                    # Add new data to cache
                    self.cache_data.update({key: item})
                    # Add new data to mruTracker
                    self.addToMruTracker(key)
                    # Remove data from MRU Tracker
                    self.mruTracker.pop(keyToDiscard)
                else:
                    self.cache_data.update({key: item})
                    if len(self.mruTracker) == 0:
                        self.mruTracker[key] = 1
                    else:
                        self.addToMruTracker(key)
            else:
                self.cache_data.update({key: item})

    def get(self, key):
        '''
        Returns the Value of a Key in the cache_data
        '''
        value = self.cache_data.get(key)

        if value:
            keyPriorityNo = self.mruTracker.get(key)
            mruNo = max(self.mruTracker.values())
            if keyPriorityNo < mruNo:
                self.mruTracker[key] = mruNo + 1

        return value
