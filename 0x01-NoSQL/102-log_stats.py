#!/usr/bin/env python3
'''script that provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_coll = client.logs.nginx
    out = f'{nginx_coll.count_documents({})} logs\nMethods:\n'

    for m in METHODS:
        count = nginx_coll.count_documents({'method': m})
        out += f'\tmethod {m}: {count}\n'
    count = nginx_coll.count_documents({'method': 'GET', 'path': '/status'})
    out += f'{count} status check\nIPs:\n'
    pipelines = [
            {
                '$group': {'_id': '$ip', 'count': {'$count': {}}}
            },
            {
                '$sort': {'count': -1}
            },
            {
                '$limit': 10
            }
    ]
    # Equavelent aggregation in SQL(it's even harder -_-)
    '''
    SELECT ip, COUNT(*) AS count FROM nginx

    GROUP BY ip
    ORDER BY count DESC;
    '''
    for ip in nginx_coll.aggregate(pipelines):
        out += f"\t{ip.get('_id')}: {ip.get('count')}\n"
    print(out, end='')
