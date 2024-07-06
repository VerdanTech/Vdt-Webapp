# Standard Library
import uuid

# External Libraries
import pytest

# VerdanTech Source
from src.common.interfaces.persistence.exceptions import (
    ObjectAlreadyExists,
    ObjectNotFound,
)
from src.user.adapters.sqlalchemy.repository import UserAlchemyRepository
from src.user.domain import User
from src.user.domain.models import EmailConfirmation
from src.user.interfaces import AbstractUserRepository

pytestmark = [pytest.mark.databases]


class TestAbstractUserRepository:
    # ================================================================
    # AbstractUserRepository.add() tests
    # ================================================================
    async def test_add_already_exists(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the proper exception occurs if the user
            already exists.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        user.id = uuid.uuid4()
        with pytest.raises(ObjectAlreadyExists):
            await user_repo.add(user)

    async def test_add_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the user is added to the repository.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        await user_repo.add(user)
        result = await user_repo.get_by_username(username=user.username)
        assert (
            result is not None
            and result.id is not None
            and result.created_at is not None
            and result.username == user.username
            and result.emails == user.emails
        )

    # ================================================================
    # AbstractUserRepository.update() tests
    # ================================================================
    async def test_update_unpersisted(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure that the proper exception occurs when a user is updated
        that hasn't been added previously.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        with pytest.raises(ObjectNotFound):
            await user_repo.update(user)

    async def test_update_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the user is updated successfully.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        user = await user_repo.add(user)

        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        new_username = "new_username"
        new_email = "new_email"
        user.username = new_username
        user.emails[0] = user.emails[0].transform(address=new_email)

        updated_user = await user_repo.update(user)
        persisted_user = await user_repo.get_by_id(id=user.id_or_error())

        assert (
            persisted_user is not None
            and persisted_user.username == updated_user.username == new_username
            and persisted_user.emails[0].address
            == updated_user.emails[0].address
            == new_email
        )

    # ================================================================
    # AbstractUserRepository.delete() tests
    # ================================================================
    async def test_delete_unpersisted(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure that the proper exception occurs when a user is deleted
        that hasn't been added previously.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        with pytest.raises(ObjectNotFound):
            await user_repo.delete(user)

    async def test_delete_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the user is deleted successfully.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        user = await user_repo.add(user)

        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        await user_repo.delete(user)
        persisted_user = await user_repo.get_by_id(id=user.id_or_error())

        assert persisted_user is None

    # ================================================================
    # AbstractUserRepository.get_by_id() tests
    # ================================================================

    async def test_get_by_id_not_found(self, user_repo: AbstractUserRepository) -> None:
        """
        Ensure None is returned if the User does not exist.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
        """
        result = await user_repo.get_by_id(id=uuid.uuid4())
        assert result is None

    async def test_get_by_id_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the User with the ID is retrieved.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        user = await user_repo.add(user)

        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        result = await user_repo.get_by_id(id=user.id_or_error())
        assert result is not None and result.id == user.id

    # ================================================================
    # AbstractUserRepository.get_by_username() tests
    # ================================================================

    async def test_get_by_username_not_found(
        self, user_repo: AbstractUserRepository
    ) -> None:
        """
        Ensure None is returned if the User does not exist.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
        """
        result = await user_repo.get_by_username(username="nonexistant_username")
        assert result is None

    async def test_get_by_username_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the User with the username is retrieved.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        user = await user_repo.add(user)
        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        result = await user_repo.get_by_username(username=user.username)
        assert (
            result is not None
            and result.id == user.id
            and result.username == user.username
        )

    # ================================================================
    # AbstractUserRepository.get_by_email_address() tests
    # ================================================================

    async def test_get_by_email_address_not_found(
        self, user_repo: AbstractUserRepository
    ) -> None:
        """
        Ensure None is returned if user does not exist.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
        """
        result = await user_repo.get_by_email_address(email_address="test@test.com")
        assert result is None

    async def test_get_by_email_address_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the user with the email address is retrieved.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        await user_repo.add(user)
        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        result = await user_repo.get_by_email_address(
            email_address=user.emails[0].address
        )
        assert result is not None and result.emails[0].address == user.emails[0].address

    # ================================================================
    # AbstractUserRepository.get_by_email_confirmation_key() tests
    # ================================================================

    async def test_get_by_email_confirmation_key_not_found(
        self, user_repo: AbstractUserRepository
    ) -> None:
        """
        Ensure None is returned if user does not exist.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
        """
        result = await user_repo.get_by_email_confirmation_key(key=uuid.uuid4())
        assert result is None

    async def test_get_by_email_confirmation_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the user with the email confirmation key is retrieved.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        key = uuid.uuid4()
        user.emails[0] = user.emails[0].transform(confirmation=EmailConfirmation(key))
        await user_repo.add(user)
        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        result = await user_repo.get_by_email_confirmation_key(key=key)
        assert (
            result is not None
            and result.emails[0].confirmation is not None
            and result.emails[0].confirmation.key == key
        )

    # ================================================================
    # AbstractUserRepository.get_by_password_reset_confirmation() tests
    # ================================================================
    async def test_get_by_password_reset_confirmation_not_found(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure None is returned if user does not exist.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        user = await user_repo.add(user)
        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        result = await user_repo.get_by_password_reset_confirmation(
            user_id=user.id_or_error(), key=uuid.uuid4()
        )
        assert result is None

    async def test_get_by_password_reset_confirmation_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """
        Ensure the user with the password reset confirmation is retrieved.

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        key = uuid.uuid4()
        user.password_reset_create(key=key)
        user = await user_repo.add(user)
        if isinstance(user_repo, UserAlchemyRepository):
            await user_repo.session.commit()

        result = await user_repo.get_by_password_reset_confirmation(
            user_id=user.id_or_error(), key=key
        )
        assert (
            result is not None
            and result.password_reset_confirmation is not None
            and result.password_reset_confirmation.key == key
        )

    # ================================================================
    # AbstractUserRepository.username_exists() tests
    # ================================================================

    @pytest.mark.parametrize(
        ("username_exists", "expected_output"), [(True, True), (False, False)]
    )
    async def test_username_exists_success(
        self,
        username_exists: bool,
        expected_output: bool,
        user_repo: AbstractUserRepository,
        user: User,
    ) -> None:
        """
        Ensure the existence of the field is returned

        Args:
            username_exists (bool): whether to pre-populate
                the repository with the user.
            expected_output (bool): the expected output of
                the repository method.
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        if username_exists:
            await user_repo.add(user)

        result = await user_repo.username_exists(username=user.username)

        assert result == expected_output

    # ================================================================
    # AbstractUserRepository.email_exists() tests
    # ================================================================

    @pytest.mark.parametrize(
        ("email_exists", "expected_output"), [(True, True), (False, False)]
    )
    async def test_email_exists_success(
        self,
        email_exists: bool,
        expected_output: bool,
        user_repo: AbstractUserRepository,
        user: User,
    ) -> None:
        """
        Ensure the existence of the field is returned.

        Args:
            email_exists (bool): whether to pre-populate
                the repository with the user.
            expected_output (bool): the expected output of
                the repository method.
            user_repo (AbstractUserRepository): fixture providing
                repository to test.
            user (User): user factory fixture.
        """
        if email_exists:
            await user_repo.add(user)

        result = await user_repo.email_exists(email_address=user.emails[0].address)

        assert result == expected_output
