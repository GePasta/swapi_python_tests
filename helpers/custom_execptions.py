"""Module for custom exceptions"""


class ModelException(Exception):
    """Class for Model Exception with return message."""

    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return f'ModelException: {self.message}'


class ServerException(Exception):
    """Class for Server Exception with return message."""

    def __init__(self, timeout: int):
        self.timeout = timeout

    def __str__(self) -> str:
        return f'ServerException: HTTP Server was not ready in {self.timeout} seconds'
