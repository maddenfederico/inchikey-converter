import io
import pytest
from convert_to_inchikey import convert_to_inchikey


def test_convert_success():
    input_list = ['methane', 'ethane', 'ethanol', 'glucose']
    desired_output = [
        'methane\tVNWKTOKETHGBQD-UHFFFAOYSA-N',
        'ethane\tOTMSDBZUPAUEDD-UHFFFAOYSA-N',
        'ethanol\tLFQSCWFLJHTTHZ-UHFFFAOYSA-N',
        'glucose\tGZCGUPFRVQAUEE-SLPGGIOYSA-N'
    ]
    input_stream = io.StringIO('\n'.join(input_list))
    assert(convert_to_inchikey(input_stream) == desired_output)

def test_convert_failure():
    input_list = ['methane', 'metabolomics', 'ethanol', 'coronavirus']
    desired_output = [
        'methane\tVNWKTOKETHGBQD-UHFFFAOYSA-N',
        'metabolomics\t0',
        'ethanol\tLFQSCWFLJHTTHZ-UHFFFAOYSA-N',
        'coronavirus\t0'
    ]
    input_stream = io.StringIO('\n'.join(input_list))
    assert(convert_to_inchikey(input_stream) == desired_output)

def test_rate_limit():
    input_list = ['methane'] * 100
    desired_output = ['methane\tVNWKTOKETHGBQD-UHFFFAOYSA-N'] * 100

    input_stream = io.StringIO('\n'.join(input_list))
    assert(convert_to_inchikey(input_stream) == desired_output)