#!/usr/bin/env python3
'''
A simple pagination
'''
import csv
import math
from typing import Tuple, List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns a tuple of size two containing a start index and
    end index
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    '''
    Server class to paginate a database of popular baby names
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Get a page
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> Dict[str, object]:
        '''
        Get hypermedia
        '''
        s_index, e_index = index_range(page, page_size)
        dataset = self.dataset()
        data = self.get_page(page, page_size)

        res = {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': page + 1 if e_index < len(dataset) + 1 else None,
                'prev_page': page - 1 if s_index > 0 else None,
                'total_pages': (1 + len(dataset)) // page_size
                }
        return res
