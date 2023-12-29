#!/usr/bin/env python3
"""return in a list for those particular pagination parameters"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing
    a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    index = (start_index, end_index)
    return index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a page"""
        dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        start_index = indexes[0]
        end_index = indexes[1]
        if start_index >= len(dataset) or end_index < 0:
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Hypermedia pagination"""
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)
        has_next_page = page < total_pages
        has_prev_page = page > 1
        return {
            "page_size" : page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if has_next_page else None,
            "prev_page": page - 1 if has_prev_page else None,
            "total_pages": total_pages
        }
