def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
    - mongo_collection: pymongo collection object.
    - topic (str): topic to be searched.

    Returns:
    - List of schools with the specified topic.
    """
    
    schools = mongo_collection.find({"topics": topic})
    
    # Convert the cursor to a list of school names
    school_list = [school['name'] for school in schools if 'name' in school]
    
    return school_list
