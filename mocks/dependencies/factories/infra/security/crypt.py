# VerdanTech Source
from mocks.infra.security.mock_crypt import MockPasswordCrypt


async def provide_mock_crypt():
    """Provide a mock password crypt for dependency injection"""
    return MockPasswordCrypt()
