#!/usr/bin/env python3
"""The index_range function"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size 2 containing a start index and an end index"""
    start = (page - 1) * page_size
    return (start, start + page_size)
