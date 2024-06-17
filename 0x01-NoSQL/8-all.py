#!/usr/bin/env python3
'''Module defines `list_all` function'''
from pymongo.collection import Collection
from pymongo.cursor import Cursor


def list_all(mongo_collection: Collection) -> Cursor:
    '''lists all documents in a collection'''
    return mongo_collection.find({})
