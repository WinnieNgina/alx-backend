#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from base caching"""
    def __init__(self):
        """Class constructor"""
        super().__init__()

    def put(self, key, item):
        """Updates dictionary values"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                evicted_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", evicted_key)
                self.cache_data.pop(evicted_key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache based on key"""
        if key is None:
            return None
        result = self.cache_data.get(key, None)
        return result
