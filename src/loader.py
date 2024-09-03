from typing import Protocol
import json
from smart_open import open
import boto3
import os
import mysql.connector

class Loader(Protocol):
    
    def load(self):
        """
        push records to destination
        """
        pass

class S3Loader:
    """
    writes NDJSON to s3
    """
    def __init__(self,config):
        self.destination_bucket = config.get('destination_bucket')
        self.destination_filename = config.get('destination_filename')
        self.session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        )

    def load(self,records):
        
        with open(f's3://{self.destination_bucket}/{self.destination_filename}',
                  'w',
                  transport_params={'client': self.session.client('s3')}) as fout:
            
            for record in records:
                fout.write(json.dumps(record))
                fout.write('\n')

class MySQLLoader:
    """
    writes records into db
    """
    def __init__(self,config):
        self.config = config
        self.conn = self.get_conn()
        self.mysql_destination_table_name = config.mysql_destination_table_name

    def get_conn(self):
        """
        returns a mysql connection
        """

        connection = mysql.connector.connect(
            host=self.config.mysql_host,
            user=self.config.mysql_user,
            password=self.config.mysql_password,
            database=self.config.mysql_db)    
        
        return connection


    def load(self, records, batch_size=1000):
        """
        running short on time,  GPT4 wrote this function and I just tweaked it a bit
        i asked: 'write me a python 3.11 function that takes a generator composed of dictionaries and writes it to a MySQL 8 table'

        Writes data from a generator of dictionaries to a MySQL table.
        
        :param records: A generator yielding dictionaries where keys are column names and values are the data.
        :param db_config: A dictionary containing MySQL database configuration (host, user, password, database).
        :param table_name: The name of the table to write data into.
        :param batch_size: The number of rows to insert in one batch (default is 1000).
        """

        with self.conn:
            with self.conn.cursor() as cursor:
                
                # Fetch the first item to get the columns
                first_item = next(records, None)
                if first_item is None:
                    return

                columns = first_item.keys()
                columns_str = ", ".join(columns)
                placeholders = ", ".join(["%s"] * len(columns))
                insert_query = f"INSERT INTO {self.mysql_destination_table_name} ({columns_str}) VALUES ({placeholders})"
                
                # Batch insert
                batch = []
                for record in records:
                    batch.append(tuple(record[col] for col in columns))
                    
                    if len(batch) >= batch_size:
                        cursor.executemany(insert_query, batch)
                        self.conn.commit()
                        batch.clear()
                
                # Insert any remaining records
                if batch:
                    cursor.executemany(insert_query, batch)
                    self.conn.commit()
        

class LocalLoader:
    """
    writes NDJSON to flatfile
    used it test writing locally
    """
    
    def __init__(self,config):
        self.destination_filename = config.runtime_config.get('destination_filename')

    def load(self,records):

        with open(self.destination_filename,'w') as fout:
            for record in records:
                fout.write(json.dumps(record))
                fout.write('\n')