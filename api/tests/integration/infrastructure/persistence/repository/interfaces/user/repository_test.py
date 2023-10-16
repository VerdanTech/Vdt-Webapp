import pytest
from src.verdantech_api.domain.interfaces.persistence.user import AbstractUserRepository
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.values import Email, EmailConfirmation, PasswordResetConfirmation

pytestmark = pytest.mark.integration


class TestAbstractUserRepository:
    async def test_add_success(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """Ensure the user is added to the repository

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """
        await user_repo.add(user=user)

        user = await user_repo.get_user_by_email_address(
            email_address=user.emails[0].address
        )
        assert user.id is not None

    async def test_add_already_exists(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """Ensure the proper exception occurs if the user
            already exists

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """

    async def test_get_user_by_email_address(
        self, user_repo: AbstractUserRepository, user: User
    ) -> None:
        """Ensure the user with the email address is retrieved

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """
        await user_repo.add(user=user)

        user_result = await user_repo.get_user_by_email_address(
            email_address=user.emails[0].address
        )
        assert user_result.emails[0].address == user.emails[0].address

    async def test_get_user_by_email_address_not_found(
        self, user_repo: AbstractUserRepository
    ) -> None:
        """Ensure None is returned if user does not exist

        Args:
            user_repo (AbstractUserRepository): fixture providing
                repository to test
        """
        user_result = await user_repo.get_user_by_email_address(
            email_address="test@test.com"
        )
        assert user_result is None

    @pytest.mark.parametrize(
        ("username_exists", "expected_output"), [(True, True), (False, False)]
    )
    async def test_username_exists(
        self,
        username_exists: bool,
        expected_output: bool,
        user_repo: AbstractUserRepository,
        user: User,
    ) -> None:
        """Ensure the existence of the field is returned

        Args:
            username_exists (bool): whether to pre-populate
                the repository with the user
            expected_output (bool): the expected output of
                the repository method
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """
        if username_exists:
            await user_repo.add(user=user)

        output = await user_repo.username_exists(username=user.username)

        assert output == expected_output

    @pytest.mark.parametrize(
        ("email_exists", "expected_output"), [(True, True), (False, False)]
    )
    async def test_email_exists(
        self,
        email_exists: bool,
        expected_output: bool,
        user_repo: AbstractUserRepository,
        user: User,
    ) -> None:
        """Ensure the existence of the field is returned

        Args:
            email_exists (bool): whether to pre-populate
                the repository with the user
            expected_output (bool): the expected output of
                the repository method
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """
        if email_exists:
            await user_repo.add(user=user)

        output = await user_repo.email_exists(email_address=user.emails[0].address)

        assert output == expected_output

    @pytest.mark.parametrize(
        ("email_confirmation_key_exists", "expected_output"),
        [(True, True), (False, False)],
    )
    async def test_email_confirmation_key_exists(
        self,
        email_confirmation_key_exists: bool,
        expected_output: bool,
        user_repo: AbstractUserRepository,
        user: User,
    ) -> None:
        """Ensure the existence of the field is returned

        Args:
            email_confirmation_key_exists (bool): whether to pre-populate
                the repository with the user
            expected_output (bool): the expected output of
                the repository method
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """
        user.emails[0] = Email(address="test@test.com", confirmation=EmailConfirmation(key="abc"))
        if email_confirmation_key_exists:
            await user_repo.add(user=user)

        output = await user_repo.email_confirmation_key_exists(key=user.emails[0].confirmation.key)

        assert output == expected_output

    @pytest.mark.parametrize(
        ("password_reset_confirmation_exists", "expected_output"),
        [(True, True), (False, False)],
    )
    async def test_password_reset_confirmation_key_exists(
        self,
        password_reset_confirmation_exists: bool,
        expected_output: bool,
        user_repo: AbstractUserRepository,
        user: User,
    ) -> None:
        """Ensure the existence of the field is returned

        Args:
            password_reset_confirmation_exists (bool): whether to pre-populate
                the repository with the user
            expected_output (bool): the expected output of
                the repository method
            user_repo (AbstractUserRepository): fixture providing
                repository to test
            user (User): factory fixture providing user
        """
        user.password_reset_confirmation = PasswordResetConfirmation(key="abc")
        if password_reset_confirmation_exists:
            await user_repo.add(user=user)

        output = await user_repo.password_reset_confirmation_key_exists(
            key=user.password_reset_confirmation.key
        )

        assert output == expected_output
