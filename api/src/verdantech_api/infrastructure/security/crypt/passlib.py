from litestar.utils.sync import AsyncCallable
from passlib.context import CryptContext

password_crypt_context = CryptContext(schemes=["argon2"], deprecated="auto")


class PasslibPasswordCrypt:
    async def get_password_hash(
        self,
        plain_password: str | bytes,
    ) -> str:
        return await AsyncCallable(password_crypt_context.hash)(secret=plain_password)

    async def verify_password(
        self,
        plain_password: str | bytes,
        hashed_password: str,
    ) -> bool:
        valid, _ = await AsyncCallable(password_crypt_context.verify_and_update)(
            secret=plain_password,
            hash=hashed_password,
        )
        return bool(valid)
