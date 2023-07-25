#!/usr/bin/env python3
"""MRU Caching."""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Most recently used cache system."""

    def __init__(self):
        """Initialize a LRUCache."""
        super().__init__()
        self.recent = deque()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item
            item: The item to be added
        """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.recent.remove(key)
        if len(self.cache_data) >= self.MAX_ITEMS:
            rm_key = self.recent.pop()
            del self.cache_data[rm_key]
            print(f"DISCARD: {rm_key}")
        self.recent.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.recent.remove(key)
        self.recent.append(key)
        return self.cache_data[key]
