#!/usr/bin/env python3
"""csv 2 json"""

import csv
import json


def convert_csv_to_json(filename):
    """attempt to convert the csv to json"""
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True

    except (OSError, csv.Error, ValueError, TypeError):
        return False
