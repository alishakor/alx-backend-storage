#!/usr/bin/env python3

"""
This module contains a function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    Args:
        topic: topic been searched for
        mongo_collection: pymongo collection object
    Returns:
        school_list: List of school
    """
    searching = ({"topics": topic})
    school_list = mongo_collection.find(searching)
    return school_list
