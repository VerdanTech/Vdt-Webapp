
class MockPasswordCrypt:
    async def get_password_hash(
        self,
        plain_password: str | bytes,
    ) -> str:
        return f"{plain_password}::hash"

    async def verify_password(
        self, plain_password: str | bytes, hashed_password: str
    ) -> bool:
        return f"{plain_password}::hash" == hashed_password
