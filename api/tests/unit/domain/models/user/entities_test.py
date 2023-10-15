from datetime import datetime
from typing import ContextManager, List

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.exceptions import (
    EmailConfirmationKeyNotFound,
    PasswordAlreadySetError,
)
from src.verdantech_api.domain.models.user.values import (
    Email,
    EmailConfirmation,
    PasswordResetConfirmation,
)


class TestUser:
    def test___post_init__(self) -> None:
        """Ensure the post init hook on the entity
        is called and sets the normalized username
        """
        user = User(username="TestUsername")
        assert user.username_norm == "testusername"
        assert user.emails == []
        assert user.memberships == []

    def test_set_username(self, user: User) -> None:
        """Ensure the lowercase username is saved into
        the user object

        Args:
            user (User): user object to test on (pytest fixture)
        """
        username = "TestUsername"
        user.set_username(username=username)
        assert user.username == username
        assert user.username_norm == username.lower()

    def test_add_email(self, user: User) -> None:
        """Ensure the correct values are set
        and email unverified

        Args:
            user (User): user (User): user object to test on (pytest fixture)
        """
        address = "TestEmail@Test.com"
        primary = False
        key = "aBcDeFg"

        user.add_email(address=address, primary=primary, key=key)

        assert user.emails[0].address == address
        assert user.emails[0].primary == primary
        assert user.emails[0].confirmation.key == key
        assert not user.emails[0].verified

    def test_add_verified_email(self, user: User) -> None:
        """Ensure the correct values are set
        and email verified

        Args:
            user (User): user (User): user object to test on (pytest fixture)
        """

        address = "TestEmail@Test.com"
        primary = False

        user.add_verified_email(address=address, primary=primary)

        assert user.emails[0].address == address
        assert user.emails[0].primary == primary
        assert user.emails[0].confirmation is None
        assert user.emails[0].verified

    def test_new_email_verification(self, user: User, mocker: MockerFixture) -> None:
        """Ensure the specified email is replaced with the result of
            email.new_confirmation

        Args:
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        mocker.patch(
            "src.verdantech_api.domain.models.user.values.Email.new_confirmation",
            return_value=Email(
                address="test2@test.com",
                verified=False,
                confirmation=EmailConfirmation(
                    key="abc", created_at=datetime(2023, 1, 1, 1, 1)
                ),
            ),
        )
        existing_emails = [
            Email(address="test1@test.com", verified=False),
            Email(address="test2@test.com", verified=False),
        ]
        expected_result = [
            Email(address="test1@test.com", verified=False),
            Email(
                address="test2@test.com",
                verified=False,
                confirmation=EmailConfirmation(
                    key="abc", created_at=datetime(2023, 1, 1, 1, 1)
                ),
            ),
        ]
        user.emails = existing_emails

        user.new_email_verification(address="test2@test.com", key="abc")

        assert user.emails == expected_result

    def test_new_password_reset(self, user: User) -> None:
        """Ensure the password reset is added to the user object

        Args:
            user (User): user factory fixture
        """
        user.password_reset_confirmation = None
        key = "abc"

        user.new_password_reset(key=key)

        assert user.password_reset_confirmation.key == key

    def test_verify_email(self, user: User, mocker: MockerFixture) -> None:
        """Ensure the correct user sub-functions are called

        Args:
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        mock_unverified_email = mocker.MagicMock(spec=Email)
        mock_get_email_by_confirmation_key = mocker.patch.object(
            user, "get_email_by_confirmation_key", return_value=mock_unverified_email
        )
        mock_verified_email = mocker.MagicMock(spec=Email)
        mock_unverified_email.verify.return_value = mock_verified_email
        mock_set_primary_email = mocker.patch.object(user, "set_primary_email")

        user.verify_email(key="abc")

        mock_get_email_by_confirmation_key.assert_called_once_with(key="abc")
        mock_unverified_email.check_confirmation_expired.assert_called_once()
        mock_unverified_email.verify.assert_called_once()
        mock_set_primary_email.assert_called_once_with(mock_verified_email)

    async def test_reset_password(self, user: User, mocker: MockerFixture) -> None:
        """Ensure that the set password method is called and the password
            reset confirmation is set to None

        Args:
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        mock_set_password = mocker.patch.object(user, "set_password")
        user.password_reset_confirmation = PasswordResetConfirmation(key="abc")
        new_password = "new_password"
        mock_password_crypt = mocker.Mock()

        await user.reset_password(
            new_password=new_password, password_crypt=mock_password_crypt
        )

        mock_set_password.assert_awaited_once_with(
            password=new_password, password_crypt=mock_password_crypt, overwrite=True
        )
        assert user.password_reset_confirmation == None

    @pytest.mark.parametrize(
        ("emails", "expected_output"),
        [
            # Test case: no verified emails, verified is False
            (
                [
                    Email(address="test@test.com", verified=False),
                    Email(address="test@test.com", verified=False),
                ],
                False,
            ),
            # Test case: at least one verified email, verified is True
            (
                [
                    Email(address="test@test.com", verified=False),
                    Email(address="test@test.com", verified=True),
                ],
                True,
            ),
        ],
    )
    def test_is_verified(
        self, emails: List[Email], expected_output: bool, user: User
    ) -> None:
        """Ensure verified is True if at least one email
            is verified, False if not

        Args:
            emails (List[Email]): emails to add on the user
            expected_output (bool): expected user.verified output
            user (User): user factory fixture
        """
        user.emails = emails

        assert user.is_verified() == expected_output

    @pytest.mark.parametrize(
        (
            "now",
            "created_at",
            "expiry_time_hours",
            "verified",
            "expected_result",
        ),
        [  # Test case: user is older than expiry_time_hours
            # and not verified, expired is true
            (
                datetime(2023, 1, 1, 12, 0),
                datetime(2023, 1, 1, 10, 0),
                1,
                False,
                True,
            ),
            # Test case: user is older than expiry_time_hours
            # and is verified, expired is false
            (
                datetime(2023, 1, 1, 12, 0),
                datetime(2023, 1, 1, 10, 0),
                1,
                True,
                False,
            ),
            # Test case: user is not older than expiry_time_hours
            # and is not verified, expired is false
            (
                datetime(2023, 1, 1, 12, 0),
                datetime(2023, 1, 1, 11, 0),
                1,
                False,
                False,
            ),
            # Test case: user is not older than expiry_time_hours
            # and is verified, expired is false
            (
                datetime(2023, 1, 1, 12, 0),
                datetime(2023, 1, 1, 11, 0),
                1,
                True,
                False,
            ),
        ],
    )
    def test_is_expired(
        self,
        now: datetime,
        created_at: datetime,
        expiry_time_hours: int,
        verified: bool,
        expected_result: bool,
        user: User,
        mocker: MockerFixture,
    ) -> None:
        """Ensure the user is expired if and only if it is older
            than expiry time hours and is not verified

        Args:
            now (datetime): mock datetime.now()
            created_at (datetime): user creation time
            expiry_time_hours (int): application setting
            verified (bool): mock verified flag on user
            expected_result (bool): expected expiry check result
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        mock_datetime = mocker.patch(
            "src.verdantech_api.domain.models.user.entities.datetime"
        )
        mock_datetime.now.return_value = now
        user.created_at = created_at
        mock_is_verified = mocker.patch.object(
            user, "is_verified", return_value=verified
        )

        assert user.is_expired(expiry_time_hours=expiry_time_hours) == expected_result
        mock_is_verified.assert_called_once()

    @pytest.mark.parametrize(
        (
            "emails",
            "key",
            "expected_result",
            "expected_error_context",
        ),
        [
            # Test case: email with confirmation key exists
            # in user.emails, email is returned and no error raised
            (
                [
                    Email(
                        address="test1@test.com",
                        confirmation=EmailConfirmation(key="abc", created_at=None),
                    ),
                    Email(
                        address="test2@test.com",
                        confirmation=EmailConfirmation(key="abc", created_at=None),
                    ),
                ],
                "abc",
                Email(
                    address="test2@test.com",
                    confirmation=EmailConfirmation(key="abc", created_at=None),
                ),
                None,
            ),
            # Test case: email with confirmation key does not
            # exist in user.emails, correct error is raised
            (
                [
                    Email(
                        address="test@test.com",
                        confirmation=EmailConfirmation(key="abc", created_at=None),
                    ),
                ],
                "123",
                None,
                EmailConfirmationKeyNotFound,
            ),
        ],
        indirect=["expected_error_context"],
    )
    def test_get_email_by_confirmation_key(
        self,
        emails: List[Email],
        key: str,
        expected_result: Email,
        expected_error_context: ContextManager,
        user: User,
    ) -> None:
        """Ensure the email with the confirmation key is
            found and returned, otherwise an error is raised

        Args:
            emails (List[Email]): existing emails on he user
            key (str): key to attempt search for
            expected_result (Email): expected function return
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            user (User): user factory fixture
        """
        user.emails = emails

        with expected_error_context as error:
            email = user.get_email_by_confirmation_key(key=key)
            if error is None:
                assert email == expected_result

    def test_set_primary_email(self, user: User, mocker: MockerFixture) -> None:
        """Ensure that the given email is make primary and inserted
            at the front of the email list, while all other emails
            are unprimary

        Args:
            user (User): user factory fixture
            mocker (MockerFixture): pytest-mock
        """
        existing_primary_email = Email(address="test1@test.com", primary=True)
        existing_unprimary_email = Email(address="test2@test.com", primary=False)
        mocker.patch(
            "src.verdantech_api.domain.models.user.values.Email.make_unprimary",
            return_value=Email(address="test1@test.com", primary=False),
        )
        mocker.patch(
            "src.verdantech_api.domain.models.user.values.Email.make_primary",
            return_value=Email(address="test2@test.com", primary=True),
        )
        user.emails = [existing_primary_email, existing_unprimary_email]

        user.set_primary_email(existing_unprimary_email)

        assert user.emails == [
            Email(address="test2@test.com", primary=True),
            Email(address="test1@test.com", primary=False),
        ]

    def test_remove_oldest_emails(self, user: User) -> None:
        """Ensure the oldest emails over max emails removed
            and email list order is preserved

        Args:
            user (User): user factory fixture
        """
        max_emails = 2
        user.emails = [
            Email(address="test1@test.com", verified_at=datetime(2024, 1, 1, 1, 1)),
            Email(address="test2@test.com", verified_at=datetime(2023, 1, 1, 1, 1)),
            Email(address="test3@test.com", verified_at=datetime(2025, 1, 1, 1, 1)),
        ]

        user.remove_oldest_emails(max_emails)

        assert user.emails == [
            Email(address="test1@test.com", verified_at=datetime(2024, 1, 1, 1, 1)),
            Email(address="test3@test.com", verified_at=datetime(2025, 1, 1, 1, 1)),
        ]

    @pytest.mark.parametrize(
        ("existing_password", "password", "overwrite", "expected_error_context"),
        [
            # Test case: no existing password -> no error
            (None, "TestPassword", False, None),
            # Existing password -> error
            ("ExistingPassword", "TestPassword", False, PasswordAlreadySetError),
            # Existing password but overwrite = True -> no error
            ("ExistingPassword", "TestPassword", True, None),
        ],
        indirect=["expected_error_context"],
    )
    async def test_set_password(
        self,
        existing_password: str,
        password: str,
        overwrite: bool,
        expected_error_context: ContextManager,
        user: User,
        mock_password_crypt: AbstractPasswordCrypt,
    ) -> None:
        """Ensure the password is set, and error is raised if
            password already exists and overwrite is not specified

        Args:
            existing_password (str): pre-existing user password
            password (str): new password
            overwrite (bool): explicit password overwrite permission
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            user (User): user object to test on (pytest fixture)
            mock_password_crypt (AbstractPasswordCrypt): (pytest fixture)
        """
        if existing_password:
            user._password_hash = existing_password

        with expected_error_context as error:
            await user.set_password(
                password=password,
                password_crypt=mock_password_crypt,
                overwrite=overwrite,
            )
            if error is None:
                assert user._password_hash == f"{password}::hash"

    @pytest.mark.parametrize(
        ("existing_password", "password", "expected_result"),
        [
            ("TestPassword", "TestPassword", True),
            ("TestPasword", "NotTestPassword", False),
        ],
    )
    async def test_verify_password(
        self,
        existing_password: str,
        password: str,
        expected_result: bool,
        user: User,
        mock_password_crypt: AbstractPasswordCrypt,
    ) -> None:
        """Ensure the function compares the input with
        password hash correctly

        Args:
            existing_password (str): existing user password
            password (str): input for comparison
            expected_result (bool): expected result of comparison
            user (User): user object to test on (pytest fixture)
            mock_password_crypt (AbstractPasswordCrypt): (pytest fixture)
        """
        user._password_hash = await mock_password_crypt.get_password_hash(
            plain_password=existing_password
        )

        assert (
            await user.verify_password(
                password=password, password_crypt=mock_password_crypt
            )
            == expected_result
        )
