from src.interfaces.email.client import AbstractEmailClient


class BaseEmailEmitter:
    def __init__(self, client: AbstractEmailClient) -> None:
        self.client = client
