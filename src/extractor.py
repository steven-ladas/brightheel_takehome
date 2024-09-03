from typing import Protocol
import csv
import time

class Extractor(Protocol):
    
    def extract(self):
        """
        extracts records
        """
        pass

class csvExtractor:
    
    def __init__(self,config):
        self.source_name = config.runtime_config.get('source_name')
        self.source_filename = config.runtime_config.get('source_filename')
        

    def extract(self):
        """
        returns a generator of each source record in the csv as a dictionary
        adds some meta while doing so
        """

        source_extract_time = int(time.time())

        with open(self.source_filename,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, record in enumerate(reader,start=1):
                record.update(
                    {
                        'source_name': self.source_name,
                        'source_filename': self.source_filename,
                        'source_row_number': i,
                        'source_extract_time': source_extract_time
                    }
                )
                yield record