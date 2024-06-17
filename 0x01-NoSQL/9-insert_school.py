#!/usr/bin/env python3
'''Module defines `list_all` function'''
from typing import Dict
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: Dict) -> str:
    '''inserts a new document in a collection based on kwargs'''
    return mongo_collection.insert_one(kwargs).inserted_id
