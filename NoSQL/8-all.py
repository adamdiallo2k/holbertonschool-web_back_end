#!/usr/bin/env python3
""" commented function """

def list_all(mongo_collection):
    """ that lists all documents in a collection: """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    else:
        return list(documents)
