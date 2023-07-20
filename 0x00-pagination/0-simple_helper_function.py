#!/usr/bin/env python3
"""Simple helper function."""


def index_range(page: int, page_size: int) -> tuple:
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
