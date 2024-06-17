#!/usr/bin/env python3
'''Module defines `list_all` function'''
from typing import List
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List:
    '''lists all documents in a collection'''
    return [doc for doc in mongo_collection.find({})]
