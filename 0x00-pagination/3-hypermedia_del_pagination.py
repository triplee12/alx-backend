#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import Any, List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize server."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE, mode="r", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve data from dataset.

        Args:
            index (int): the page index
            page_size (int): the page size (content size)

        Returns:
            Dict: hypermeta detail of the page
        """
        data: Dict[int, List] = self.indexed_dataset()
        # Validate index is in a valid range
        if index is not None:
            assert index >= 0, "Index must be a non-negative integer."
            assert index < len(data), "Index is out of range."

        # Calculate the current start index of the return page
        if index is None:
            index = 0
        current_index: int = index

        # Calculate the next index to query with
        next_index: int = current_index + page_size

        # Get the actual page of the dataset
        current_page_data: list = []
        for i in range(current_index, min(next_index, len(data))):
            if i in data:
                current_page_data.append(data[i])

        # Create the dictionary with the required key-value pairs
        result_dict: Dict[str, Any] = {
            'index': current_index,
            'data': current_page_data,
            'page_size': page_size,
            'next_index': next_index
        }
        return result_dict
