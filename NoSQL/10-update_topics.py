#!/usr/bin/env python3
""" commented function """


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on its name.

    Args:
    - mongo_collection: pymongo collection object.
    - name (str): school name to update.
    - topics (list of str): list of topics approached in the school.

    Returns:
    - The count of updated documents.
    """
    
    result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
    
    return result.modified_count
