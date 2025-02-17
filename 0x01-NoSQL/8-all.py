#!/usr/bin/env python3
"""
This module have a utility function that list all document
"""
import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
