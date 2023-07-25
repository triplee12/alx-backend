#!/usr/bin/env python3
"""Basic dictionary."""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic cache extends from BaseCaching."""

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item
            item: The item to be added
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
