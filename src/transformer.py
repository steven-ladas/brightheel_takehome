from typing import Protocol
from utils.utils import remove_non_numbers
from records.destination_record import DestinationRecord
import json
import datetime

class Transformer(Protocol):
    
    def transform(self):
        """
        transforms records
        """
        pass

class sourceOneTransformer:

    def __init__(self, config):
        self.config = config

    def transform(self,records):

        for record in records:
            d = dict()

            d.update({
                    #meta
                    'source_name': record.get('source_name'),
                    'source_filename': record.get('source_filename'),
                    'source_record_number': record.get('source_record_number'),
                    'source_extract_time':  record.get('source_extract_time'),

                    #from source
                    'company': record.get('Name'),
                    'license_type': record.get('Credential Type'),
                    'license_number': record.get('Credential Number'),
                    'license_status': record.get('Status'),
                    'certificate_expiration_date': get_datetime_from_mmddyy(record.get('Expiration Date')),
                    'address1': record.get('Address'),
                    'state': record.get('State'),
                    'county': record.get('County'),
                    'phone': remove_non_numbers(record.get('Phone')),
                    'first_name': record.get('Primary Contact Name').split()[0],
                    'last_name': record.get('Primary Contact Name').split()[1],
                    'title': record.get('Primary Contact Role')
            })

            transformed_record = DestinationRecord(**d)

            yield transformed_record.dict()


class sourceTwoTransformer:
    
    def __init__(self, config):
        self.config = config
    
    def transform(self,records):
        
        for record in records:
            d = dict()

            d.update({
                    #meta
                    'source_name': record.get('source_name'),
                    'source_filename': record.get('source_filename'),
                    'source_record_number': record.get('source_record_number'),
                    'source_extract_time':  record.get('source_extract_time'),

                    #from source
                    'license_type': record.get('Type License').split('-')[0].strip(),
                    'license_number': record.get('Type License').split('-')[1].strip(),
                    'company': record.get('Company'),
                    'accepts_financial_aid':  record.get('Accepts Subsidy'),              
                    'schedule': smash(record,['Year Round','School Year Only','Daytime Hours','Evening Hours','Mon','Tues','Wed','Thurs','Friday','Saturday','Sunday']),
                    'first_name': record.get('Primary Caregiver').split()[0],
                    'last_name': record.get('Primary Caregiver').split()[1],
                    'title': ' '.join(record.get('Primary Caregiver').split()[2:]),
                    'phone': remove_non_numbers(record.get('Phone')),
                    'email': record.get('Email'),   
                    'address1': record.get('Address1'),  
                    'address2': record.get('Address2'),  
                    'city': record.get('City'),  
                    'state': record.get('State'),  
                    'zip': record.get('Zip'),
                    'capacity': record.get('Total Cap'),
                    'ages_served': smash(record,['Ages Accepted 1','AA2','AA3','AA4'])
            })

            transformed_record = DestinationRecord(**d)

            yield transformed_record.dict()   

class sourceThreeTransformer:
    
    def __init__(self, config):
        self.config = config
    
    def transform(self,records):
        
        for record in records:
            d = dict()

            d.update({
                    #meta
                    'source_name': record.get('source_name'),
                    'source_filename': record.get('source_filename'),
                    'source_record_number': record.get('source_record_number'),
                    'source_extract_time':  record.get('source_extract_time'),

                    #from source
                    'license_type': record.get('Type'),
                    'license_number': record.get('Operation'),
                    'company': record.get('Operation Name'),
                    'address1': record.get('Address'),  
                    'city': record.get('City'),
                    'state': record.get('State'), 
                    'zip': record.get('Zip'),
                    'county': record.get('County'),
                    'phone': remove_non_numbers(record.get('Phone')),
                    'license_status': record.get('Status'), 
                    'license_issued': get_datetime_from_mmddyy(record.get('Issue Date')),
                    'capacity': record.get('capacity'),
                    'email': record.get('Email Address'),  
                    #'facility_type': record.get('Facility ID'),  not sure the ID is the "type" so not including in mapping
                    'ages_served': smash(record,['Infant','Toddler','Preschool','School'])
            })

            transformed_record = DestinationRecord(**d)

            yield transformed_record.dict()  


"""
misc functions
"""

def get_datetime_from_mmddyy(s):
    """
    source1 datetime converter
    
    comes in like mm/dd/yy
    return as yyyy-mm-dd

    assuming 21st century dates
    """

    try:
        mm,dd,yy = s.split('/')
        return f'20{yy}-{mm}-{dd}'
    except:
        return None

def smash(record,smash_list):
    """
    wild wild west for schedules and ages served.
    dont have enough time to find a way standardize it so just smashing it all together

    returning json?  can't think of anything too clever here i can do with time constraint
    """

    d = dict()

    [d.update({k: record[k]}) for k in smash_list] #side effect desired

    return json.dumps(d)