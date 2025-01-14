import email
import sys
sys.path.append('../')
from database.db import Database

class Customers:
    """
    A class that handles all customer operations.

    args:
        - email: email address of the customer.
        - username: unique identifier for each customer.
        - password: 
        - first_name: first name of the customer.
        - last_name: last name of the customer.

    attributes:
        - email: email address of the customer.
        - username: unique identifier for each customer.
        - password: 
        - first_name: first name of the customer.
        - last_name: last name of the customer.

    """
    def __init__(self, username: str = None) -> None:
        self.username = username
        self.email = ""
        self.first_name = ""
        self.last_name = ""

    def get_email(self) -> str:
        return Database.get_customer_email(self.username)
    
    def set_email(self) -> str:
        self.email = Database.get_customer_email(self.username)

    def get_first_name(self) -> str:
        return Database.get_customer_first_name(self.username)
    
    def set_first_name(self) -> str:
        self.first_name = Database.get_customer_first_name(self.username)

    def get_last_name(self) -> str:
        return Database.get_customer_last_name(self.username)
    
    def set_last_name(self) -> str:
        self.last_name = Database.get_customer_last_name(self.username)

    def get_customer_details(self) -> dict:
        customer = {"username": self.username, "email": self.email, "first_name": self.first_name, "last_name": self.last_name}
        return customer
