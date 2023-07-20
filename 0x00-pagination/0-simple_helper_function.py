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
    if page == 1:
        return (0, page_size)
    return (page * 10, page * page_size)
