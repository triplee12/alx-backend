#!/usr/bin/env python3
"""FIFO caching."""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """First in First Out Cache system."""

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item
            item: The item to be added
        """
        if key is None or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            data_keys = [k for k in self.cache_data.keys()]
            rm_key = data_keys.pop(0)
            del self.cache_data[rm_key]
            print(f"DISCARD: {rm_key}")
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
