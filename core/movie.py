
import datetime
from xmlrpc.client import DateTime


class Movie:
       """
    A class that handles all movie operations.

    args:
        - title: 
        - genre:
        - duration: 
        - rating:
        - release_year:
        - price:

    attributes:
        - title: 
        - genre:
        - duration: 
        - rating:
        - release_year:
        - price:

    """
def __init__(self, title: str = None, genre: str = None, duration: DateTime = None, rating: str = None, release_year: int = None, price: int = None) -> None:
    self.title = title
    self.genre = genre
    self.duration = duration
    self.rating = rating
    self.release_year = release_year
    self.price = price

def get_title() -> str:
    pass

def set_title(self, title: str) -> None:
    pass

def get_genre() -> str:
    pass

def set_genre(self, genre: str) -> None:
    pass

def get_duration() -> datetime:
    pass

def set_duration(self, duration: datetime) -> None:
    pass

def get_rating() -> str:
    pass

def get_rating(self, rating: str) -> None:
    pass

def get_release_year() -> int:
    pass

def set_release_year(self, release_year: int) -> None:
    pass

def get_price() -> str:
    pass

def set_price(self, price: int) -> None:
    pass

def get_movie_showtimes(self, title: str) -> dict:
    pass

def get_movie_by_theater(self, title: str) -> dict:
    pass
