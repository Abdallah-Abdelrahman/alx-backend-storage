#!/usr/bin/env python3
'''Module defines `insert_school` function'''
from typing import Dict
from pymongo.collection import Collection
from bson import ObjectId


def insert_school(mongo_collection: Collection, **kwargs: Dict) -> ObjectId:
    '''inserts a new document in a collection based on kwargs'''
    return mongo_collection.insert_one(kwargs).inserted_id
