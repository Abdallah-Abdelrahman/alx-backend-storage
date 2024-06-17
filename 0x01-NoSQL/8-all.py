#!/usr/bin/env python3
'''Module defines `list_all` function'''
from typing import List


def list_all(mongo_collection) -> List:
    '''lists all documents in a collection'''
    return [doc for doc in mongo_collection.find({})]
