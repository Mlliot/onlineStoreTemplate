import sys
sys.path.append('../')
from database.db import Database

class Movies:
    """
    A class that handles all movie operations.

    args:
        - item_code
        - name
        - description
        - genre

    attributes:
        - item_code
        - name
        - description
        - genre 

    """
def __init__(self, show_code: str = None) -> None:
    self.show_code = show_code

def get_title(self) -> str:
    return Database.get_shows_movie_title(self.show_code)

def get_running_time(self) -> str:
    return Database.get_shows_running_time(self.show_code)

def get_date(self) -> str:
    return Database.get_shows_datee(self.show_code)

def get_shows_details(self) -> dict:
    movie = {"title": Database.get_shows_movie_title(self.show_code), "running_time": Database.get_shows_running_time(self.show_code), "date": Database.get_shows_datee(self.show_code)}
    return movie
