"""
Parsing csv and reading csv from the spec.
"""

import re, csv
from pathlib import Path

from getgauge.python import Table


class ProtoRow:
    def __init__(self, cells):
        self.cells = cells

class ProtoTable:
    def __init__(self, table_dict):
        self.headers = ProtoRow(table_dict['headers']['cells'])
        self.rows = [ProtoRow(row['cells']) for row in table_dict['rows']]


def parse_csv_to_gauge_table(csv_file):
    '''
    Parse the csv file into a gauge table

    Args:
        csv_file (Path object) : the object that extract_csv_file_from_spec() returns
    Return:
        Table object : Contains all the headers, rows, and columns data from the csv_file
    '''
    with csv_file.open() as f:
        headers = []
        rows = []

        lines = csv.reader(f)
        for index, row in enumerate(lines):
            if index == 0:
                headers = row
            else:
                rows.append({'cells': row})

        return Table(ProtoTable({'headers': {'cells': headers}, 'rows': rows}))



def extract_csv_file_from_spec(specification):
    '''
    Returns the csv file path specified in the .spec file

    Example:
        Sample details in spec.

        [1] # Stylists API
        [2] table:step_impl/inputs/stylists/stylists_success.csv

        return: step_impl/inputs/stylists/stylists_success.csv

    Args:
        specification (class object): specified spec file
    Returns:
        Path (Path object) : csv file path
    '''
    input_table_pattern = re.compile(r'(table(\s)*:(\s)*)(.*csv)')
    spec_file = Path(specification.file_name)
    csv_file = None

    with spec_file.open() as f:
        for line in f.readlines():
            match = input_table_pattern.match(line.strip().lower())
            # group 3 in regex contains the csv file path
            if match and match.groups()[3]:
                csv_file = Path(match.groups()[3])
                break

    return csv_file
