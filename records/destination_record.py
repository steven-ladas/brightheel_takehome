import datetime
from dataclasses import dataclass, asdict

@dataclass
class DestinationRecord:
    """
    destination record

    match what i can to here
    """
    
    #meta
    source_name: str
    source_filename: str
    source_record_number: int
    source_extract_time: int

    #fill as many as source allows
    accepts_financial_aid: str = None
    ages_served: str = None
    capacity: int = None
    certificate_expiration_date: datetime.datetime = None
    city: str = 'UNKNOWN'
    address1: str = None
    address2: str = None
    company: str = 'UNKNOWN'
    phone: str = None
    phone2: str = None
    county: str = 'UNKNOWN'
    curriculum_type: str = 'UNKNOWN'
    email: str = 'UNKNOWN'
    first_name: str = 'UNKNOWN'
    language: str = 'UNKNOWN'
    last_name: str = 'UNKNOWN'
    license_status: str = 'UNKNOWN'
    license_issued: datetime.datetime = None
    license_number: int = None
    license_renewed: datetime.datetime = None
    license_type: str = 'UNKNOWN'
    licensee_name: str = 'UNKNOWN'
    max_age: int = None
    min_age: int = None
    operator: str = 'UNKNOWN'
    provider_id: str = 'UNKNOWN'
    schedule: str = 'UNKNOWN'
    state: str = 'UNKNOWN'
    title: str = 'UNKNOWN'
    website_address: str = 'UNKNOWN'
    zip: str = 'UNKNOWN'
    facility_type: str = 'UNKNOWN'

    # convert to dictionary
    dict = asdict




    {"Operation": "1239246", "Agency Number": "", "Operation Name": "K\" Street Learning Center LLC\"", "Address": "19290 K ST", "City": "SOMERSET", "State": "TX", "Zip": "78069", "County": "BEXAR", "Phone": "830-429-1010", "Type": "Licensed Center - Child Care Program", "Status": "Full Permit", "Issue Date": "10/13/11", "Capacity": "82", "Email Address": "sylvia@kstreetlearningcenter.com", "Facility ID": "773628", "Monitoring Frequency": "", "Infant": "Y", "Toddler": "Y", "Preschool": "Y", "School": "Y", "source_name": "source3", "source_filename": "./data/source3.csv", "source_row_number": 1, "source_extract_time": 1725325593}