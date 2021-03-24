'''Python 3 script that accepts a file with a newline-separated list of chemical structure identifiers
    and outputs a newline-separated list of tab-separated identifier/inchikey pairs.
    If input cannot be resolved, will output 0 in place of an inchikey'''
'''Written by Federico Madden, 2021'''

import sys
import requests
from requests import HTTPError

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    input_compounds = f.read().splitlines()

for compound in input_compounds:
    try:
        response = requests.get(f"https://cactus.nci.nih.gov/chemical/structure/{compound}/stdinchikey")
        response.raise_for_status()
        print(f"{compound}\t{response.text.partition('=')[2]}")
    except HTTPError:
        print(f"{compound}\t0")







