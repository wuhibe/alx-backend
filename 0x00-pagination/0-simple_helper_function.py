#!/usr/bin/env python3
''' module for task 0 '''

def index_range(page: int, page_size: int) -> tuple:
    ''' start to end of last index page '''
    last: int = page_size * page
    return (last - page_size, last)
