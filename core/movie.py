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
def __init__(self, item_code: str = None) -> None:
    self.item_code = item_code

def get_title(self) -> str:
    return Database.get_theater_name(self.item_code)

def get_description(self) -> str:
    return Database.get_movie_description(self.item_code)

def get_genre(self) -> str:
    return Database.get_movie_genre(self.item_code)

def get_movie_details(self) -> dict:
    movie = {"title": Database.get_theater_name(self.item_code), "description": Database.get_movie_description(self.item_code), "genre": Database.get_movie_genre(self.item_code)}
    return movie
