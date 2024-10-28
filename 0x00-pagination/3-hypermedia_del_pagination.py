#!/usr/bin/env python3
'''
A simple pagination
'''
import csv
import math
from typing import Tuple, List, Dict, Union


class Server:
    '''
    Server class to paginate a database of popular baby names
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self,
                        index: int = None,
                        page_size: int = 10) -> Dict:
        '''
        Get hypermedia
        '''
        assert index < len(self.dataset())
        dataset = self.indexed_dataset()
        data: List[List[str]] = []
        i = 0
        while len(data) < page_size:
            row = dataset.get(index + i)
            if row:
                data.append(row)
            i += 1

        res = {
                'index': index,
                'data': data,
                'page_size': len(data),
                'next_index': index + len(data),
                }
        return res
