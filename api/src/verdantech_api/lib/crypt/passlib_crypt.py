from litestar.utils.sync import AsyncCallable
from passlib.context import CryptContext
from pydantic import SecretBytes, SecretStr

from .generic import PasswordCrypt

password_crypt_context = CryptContext(schemes=["argon2"], deprecated="auto")


class PasslibPasswordCrypt(PasswordCrypt):
    async def get_password_hash(self,
        plaintext_password: SecretBytes | SecretStr | str | bytes,
    ) -> str:
        if isinstance(plaintext_password, SecretBytes | SecretStr):
            plaintext_password = plaintext_password.get_secret_value()
        return await AsyncCallable(password_crypt_context.hash)(
            secret=plaintext_password
        )

    async def verify_password(self,
        plain_password: SecretBytes | SecretStr | str | bytes, hashed_password: str
    ) -> bool:
        if isinstance(plain_password, SecretBytes | SecretStr):
            plain_password = plain_password.get_secret_value()
        valid, _ = await AsyncCallable(password_crypt_context.verify_and_update)(
            secret=plain_password,
            hash=hashed_password,
        )
        return bool(valid)
