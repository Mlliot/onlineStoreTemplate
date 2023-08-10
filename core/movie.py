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
        self.title = ""
        self.description = ""
        self.genre = ""

    def get_title(self) -> str:
        return Database.get_movie_title(self.item_code)
    
    def set_title(self) -> str:
        self.title = Database.get_movie_title(self.item_code)

    def get_description(self) -> str:
        return Database.get_movie_description(self.item_code)

    def set_description(self) -> str:
        self.description = Database.get_movie_description(self.item_code)

    def get_genre(self) -> str:
        return Database.get_movie_genre(self.item_code)
    
    def set_genre(self) -> str:
        self.genre = Database.get_movie_genre(self.item_code)

    def get_movie_details(self) -> dict:
        movie = {"title": self.title, "description": self.description, "genre": self.genre}
        return movie
