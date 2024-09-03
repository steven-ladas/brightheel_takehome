import json

def read_runtime_config(filename):
    """
    for local use, runtime config dictionary
    """
    
    with open(filename,'r') as fin:
        config = fin.read()

        return json.loads(config)
    
def remove_non_numbers(s):
    """
    clean up phone numbers by removing all but the digits
    """

    return ''.join([i for i in s if i.isdigit()])

def get_datetime_from_mmddyy(s):
    """
    source1 datetime converter
    
    comes in like mm/dd/yy

    return as yyyy-mm-dd

    assuming 21st century dates
    """

    mm,dd,yy = s.split('/')
    return f'20{yy}-{mm}-{dd}'



