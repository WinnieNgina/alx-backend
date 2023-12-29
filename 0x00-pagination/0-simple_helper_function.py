#!/usr/bin/env python3
"""return in a list for those particular pagination parameters"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """return a tuple of size two containing
    a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    index = (start_index, end_index)
    return index
