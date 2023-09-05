#!/usr/bin/env python3
""" commented function """


def list_all(mongo_collection):
    """ that lists all documents in a collection: """
    if not db.school.find():
        return []
    else:
        return db.school.find()
