'''Python 3 script that accepts a file with a newline-separated list of chemical structure identifiers
    and outputs a newline-separated list of tab-separated identifier/inchikey pairs.
    If input cannot be resolved, will output 0 in place of an inchikey'''
'''Written by Federico Madden, 2021'''

import sys
import requests
from requests import HTTPError


def convert_to_inchikey(input_file):

    input_compounds = input_file.read().splitlines()
    output = []
    for compound in input_compounds:
        try:
            response = requests.get(f"https://cactus.nci.nih.gov/chemical/structure/{compound}/stdinchikey")
            response.raise_for_status()
            output.append(f"{compound}\t{response.text.partition('=')[2]}")
        except HTTPError:
            output.append(f"{compound}\t0")

    return output


if __name__ == "__main__":
    input_path = sys.argv[1]
    with open(input_path, 'r') as f:
        print('\n'.join(convert_to_inchikey(f)))
