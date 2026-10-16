#!/usr/bin/env python3
"""xml data"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """record the dict to xml"""
    try:
        root = ET.Element("the_data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = "" if value is None else str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)
    except (OSError, ValueError, TypeError, ET.ParseError, Exception):
        return None


def deserialize_from_xml(filename):
    """recover the dict from the xml"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        my_dict = {}
        for child in root:
            my_dict[child.tag] = "" if child.text is None else child.text
        return my_dict
    except (OSError, ET.ParseError, Exception):
        return None
