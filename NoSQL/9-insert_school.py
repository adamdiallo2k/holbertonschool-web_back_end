#!/usr/bin/env python3
""" commented function """


def insert_school(mongo_collection, **kwargs):
    """ 
    Function that inserts a new document in a collection based on kwargs 
    """
    
    # Insert an empty document and get its _id
    insertedDoc = mongo_collection.insert_one({})
    docID = insertedDoc.inserted_id
    
    # Update the document with fields from kwargs
    for key, value in kwargs.items():
        mongo_collection.update_one({"_id": docID}, {"$set": {key: value}})
    
    return docID
