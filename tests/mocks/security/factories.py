from .crypt_mock import MockPasswordCrypt


async def provide_mock_password_crypt():
    """Provide mock password crypt for dependency injection"""
    return MockPasswordCrypt()
