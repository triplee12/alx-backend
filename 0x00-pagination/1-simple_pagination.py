#!/usr/bin/env python3
"""Simple pagination."""

import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE, mode="r", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Simple helper function.

        Args:
            page (int): page to index
            page_size (int): size of the page

        Returns:
            tuple: the index of the page and the size of the page
        """
        if page <= 0 or page_size <= 0:
            raise ValueError(
                "Both page and page_size must be positive integers."
            )

        # Adjusting the start index for 1-indexed pages
        start_index: int = (page - 1) * page_size

        # Calculating the end index based on the start index and page size
        end_index: int = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page.

        Args:
            page (int): page to index
            page_size (int): size of the page

        Returns:
            List: the index of the page and the size of the page
        """
        assert isinstance(page, int) and isinstance(page_size, int) > 0
        assert page > 0 and page_size > 0
        data: List[List] = self.dataset()
        index: tuple = self.index_range(page=page, page_size=page_size)

        if page_size < len(data):
            return data[index[0]:index[1]]
        return []
