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
        self.title = ""
        self.running_time = ""
        self.date = ""

    def get_title(self) -> str:
        return Database.get_shows_movie_title(self.show_code)
    
    def set_title(self) -> str:
        self.title = Database.get_shows_movie_title(self.show_code)

    def get_running_time(self) -> str:
        return Database.get_shows_running_time(self.show_code)
    
    def set_running_time(self) -> str:
        self.running_time = Database.get_shows_running_time(self.show_code)

    def get_date(self) -> str:
        return Database.get_shows_datee(self.show_code)
    
    def set_date(self) -> str:
        self.date = Database.get_shows_datee(self.show_code)

    def get_shows_details(self) -> dict:
        movie = {"title": self.title, "running_time": self.running_time, "date": self.date}
        return movie
