# VerdanTech Source
from src.interfaces.email.client import AbstractEmailClient


class BaseEmailEmitter:
    """
    Base class for implementing Email Emitter interface.
    """

    def __init__(self, client: AbstractEmailClient) -> None:
        self.client = client
