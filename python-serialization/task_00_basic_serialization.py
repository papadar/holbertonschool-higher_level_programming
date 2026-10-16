#!/usr/bin/env python3
"""handle the data serial style"""

import json


def serialize_and_save_to_file(data, filename):
    """serialise and save the file"""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    pass


def load_and_deserialize(filename):
    """deserialise the file"""
    with open(filename, "r") as file:
        data = json.load(file)
        return data
    pass
