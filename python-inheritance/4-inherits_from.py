#!/usr/bin/python3
"""Module that checks inheritance from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
