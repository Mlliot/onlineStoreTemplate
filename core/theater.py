import sys
sys.path.append('../')
from database.db import Database

class Theaters:
       """
    A class that handles all theater operations.

    args:
        - location_code
        - name:
        - city:
        - zip_code: 

    attributes:
        - location_code
        - name:
        - city:
        - zip_code: 


    """
def __init__(self, location_code: str = None) -> None:
    self.location_code = location_code

def get_name(self) -> str:
    return Database.get_theater_name(self.location_code)

def get_city(self) -> str:
    return Database.get_theater_city(self.location_code)

def get_zip_code(self) -> str:
    return Database.get_theater_zip_code(self.location_code)

def get_theater_details(self) -> dict:
    theater = {"name": Database.get_theater_name(self.location_code), "city": Database.get_theater_city(self.location_code), "zip_code": Database.get_theater_zip_code(self.location_code)}
    return theater


