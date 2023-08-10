class Manager:
       """
    A class that handles all manager operations.

    args:
        - email: email address of the manager.
        - username: unique identifier for each manager.
        - password: 
        - first_name: first name of the manager.
        - last_name: last name of the manager.

    attributes:
        - email: email address of the manager.
        - username: unique identifier for each manager.
        - password: 
        - first_name: first name of the manager.
        - last_name: last name of the manager.

    """
def __init__(self, email: str = None, username: str = None, password: str = None, first_name: str = None, last_name: str = None) -> None:
    self.username = username
    self.password = password

    def get_username() -> str:
        return username

    def set_username(self, username: str) -> None:
        self.username = username

    def get_password() -> str:
        return password

    def set_password(self, password: str) -> None:
        self.password = password
