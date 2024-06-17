#!/usr/bin/env python3
'''Module defines `update_topics` function'''


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a school document based on the name'''
    query = {'name': name}
    update = {'$set': {'topics': topics}}
    mongo_collection.update_one(query, update)
