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
