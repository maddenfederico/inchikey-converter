# inchikey-converter

Python 3 script that accepts the path of a file with a newline-separated list of chemical structure identifiers and outputs a newline-separated list of tab-separated identifier/inchikey pairs to stdout. If input cannot be resolved, will output 0 in place of an inchikey.

Usage: `python3 convert_to_inchikey.py input_list.txt`

Requires Python 3.6 or above and the [requests](https://pypi.org/project/requests/) module 
