#!/usr/bin/env python3
'''
A basic implementation of a LFU caching system
'''


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    A LFU caching algorithm
    '''

    def __init__(self):
        '''
        Constructor method
        '''
        super().__init__()
        # self.lruTracker = {}
        self.lfuTracker = {}

    def addToLFUTracker(self, key):
        '''
        Adds a new key to the LFUTracker dict
        '''
        self.lfuTracker[key] = 1

    def removeFromLFUTracker(self, key):
        '''
        Adds a new key to the LFUTracker dict
        '''
        self.lfuTracker.pop(key)

    def put(self, key, item):
        '''
        Update or add items to cache_data
        '''
        if key is None or item is None:
            pass
        else:
            if self.get(key) is None:
                if len(self.cache_data) == self.MAX_ITEMS:
                    sortedKeys = sorted(self.lfuTracker,
                                        key=lambda key: self.lfuTracker[key])
                    keyToDiscard = list(reversed(sortedKeys))[-1]
                    print("DISCARD:", keyToDiscard)
                    # Remove data from cache
                    self.cache_data.pop(keyToDiscard)
                    # Add new data to cache
                    self.cache_data.update({key: item})
                    # Add new data to LFUTracker
                    self.addToLFUTracker(key)
                    # Remove data from LFU Tracker
                    self.removeFromLFUTracker(keyToDiscard)
                else:
                    self.cache_data.update({key: item})
                    self.addToLFUTracker(key)
            else:
                self.cache_data.update({key: item})

    def get(self, key):
        '''
        Returns the Value of a Key in the cache_data
        '''
        value = self.cache_data.get(key)

        if value:
            # keyPriorityNo = self.lruTracker.get(key)
            # mruNo = max(self.lruTracker.values())
            self.lfuTracker[key] += 1

        return value
