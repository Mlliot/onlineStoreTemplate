
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
        return title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_genre() -> str:
        return genre

    def set_genre(self, genre: str) -> None:
        self.genre = genre

    def get_duration() -> datetime:
        return duration

    def set_duration(self, duration: datetime) -> None:
        self.duration = duration

    def get_rating() -> str:
        return rating

    def set_rating(self, rating: str) -> None:
        self.rating = rating

    def get_release_year() -> int:
        return release_year

    def set_release_year(self, release_year: int) -> None:
        self.release_year = release_year

    def get_price() -> str:
        return price

    def set_price(self, price: int) -> None:
        self.price = price

    def get_movie_showtimes(self, title: str) -> dict:
        pass

    def get_movie_by_theater(self, title: str) -> dict:
        pass
