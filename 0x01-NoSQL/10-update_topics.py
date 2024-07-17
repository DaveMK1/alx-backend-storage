#!/usr/bin/env python3
"""
change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a collection's document based on the name
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
