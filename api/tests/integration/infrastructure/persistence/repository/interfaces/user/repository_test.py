from src.verdantech_api.domain.interfaces.persistence.user import (
    AbstractUserRepository,
)
from src.verdantech_api.domain.models.user.entities import User


class TestAbstractUserRepository:
    async def test_add(self, user_repo: AbstractUserRepository, user: User) -> None:
        
        await user_repo.add(user=user)
        
        user = await user_repo.get_user_by_email_address(email_address=user.email_address)
        assert user.id is not None
