#!/usr/bin/env python3
"""xml data"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """record the dict to xml"""
    root = ET.Element("the_data")
    try:
        for key, value in dictionary.items():
            child = ET.Element(root, str(key))
            child.text = str(value)
        ET.ElementTree(root).write(
            filename, encoding="utf-8", xml_declaration=True
        )
        return True
    except (OSError, ValueError, TypeError):
        return False


def deserialize_from_xml(filename):
    """recover the dict from the xml"""
    try:
        root = ET.parse(filename).getroot()
        return {child.tag: child.text for child in root}
    except (OSError, ValueError, TypeError, ET.ParseError):
        return None
