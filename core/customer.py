
class Customer:
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
def __init__(self, email: str = None, username: str = None, password: str = None, first_name: str = None, last_name: str = None) -> None:
    self.email = email
    self.username = username
    self.password = password
    self.first_name = first_name
    self.last_name = last_name

def get_username() -> str:
    pass

def set_username(self, username: str) -> None:
    pass

def get_password() -> str:
    pass

def set_password(self, password: str) -> None:
    pass

def get_email() -> str:
    pass

def set_email(self, email: str) -> None:
    pass

def get_first_name() -> str:
    pass

def set_first_name(self, first_name: str) -> None:
    pass

def get_last_name() -> str:
    pass

def set_last_name(self, last_name: str) -> None:
    pass

def forget_username(self, email: str) -> str:
    pass

def forget_password(self, email: str) -> str:
    pass

def generate_password_hash(self, password: str) -> str:
    pass
