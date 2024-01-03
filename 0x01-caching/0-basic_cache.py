#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from base caching"""
    def put(self, key, item):
        """Updates dictionary values"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache based on key"""
        if key is None:
            return None
        result = self.cache_data.get(key, None)
        return result
