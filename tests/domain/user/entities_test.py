# Standard Library
from datetime import datetime
from typing import ContextManager, List

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.domain.user import exceptions
from src.domain.user.entities import User
from src.domain.user.values import Email, EmailConfirmation, PasswordResetConfirmation
from src.interfaces.security.crypt import AbstractPasswordCrypt

pytestmark = [pytest.mark.unit]


class TestUser:
    # ======================================
    # User.email_create() tests
    # ======================================

    def test_email_create_first_no_verification(self, user: User) -> None:
        """
        Ensure that when no other emails exist and verification is
        not required, the email is created with with primary and verified as True.

        Args:
            user (User): user fixture.
        """
        user.emails = []
        email_address = "test@test.com"

        user.email_create(address=email_address, max_emails=0, verification=False)

        assert (
            user.emails[0].address == email_address
            and user.emails[0].primary is True
            and user.emails[0].verified is True
        )

    @pytest.mark.parametrize(
        ("key", "expected_error_context"),
        [
            # Test case: a confirmation key is provided, and no error is raised
            ("abc", None),
            # Test  case: no confirmation key is provided, and an error is raised
            (None, ValueError),
        ],
        indirect=["expected_error_context"],
    )
    def test_email_create_first_verification(
        self,
        key: str,
        expected_error_context: ContextManager,
        user: User,
    ) -> None:
        """
        Ensure that when no other emails exist and verification is
        required, the email is created with primary as True, verified as False,
        with an email confirmation, and an error is raised if a confirmation
        key was not provided.

        Args:
            key (str): confirmation key parameter.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            user (User): user fixture.
        """
        user.emails = []
        email_address = "test@test.com"

        with expected_error_context as error:
            user.email_create(
                address=email_address,
                max_emails=0,
                verification=True,
                email_confirmation_key=key,
            )

        if error is None:
            assert (
                user.emails[0].address == email_address
                and user.emails[0].primary is True
                and user.emails[0].verified is False
                and user.emails[0].confirmation is not None
            )

    def test_email_create_non_first_no_verification(self, user: User) -> None:
        """
        Ensure that when other emails do exist and verification is
        not required, the email is created with primary and verification
        as True, and the other emails are trimmed and made unprimary.

        Args:
            user (User): user fixture.
        """
        user.emails = [
            Email(address="test2@test.com", primary=True),
            Email(address="test3@test.com", primary=True),
        ]
        email_address = "test@test.com"

        user.email_create(address=email_address, max_emails=2, verification=False)

        assert (
            len(user.emails) == 2
            and user.emails[0].address == email_address
            and user.emails[0].primary is True
            and user.emails[0].verified is True
            and user.emails[1].primary is False
        )

    @pytest.mark.parametrize(
        ("key", "expected_error_context"),
        [
            # Test case: a confirmation key is provided, and no error is raised
            ("abc", None),
            # Test  case: no confirmation key is provided, and an error is raised
            (None, ValueError),
        ],
        indirect=["expected_error_context"],
    )
    def test_email_create_non_first_verification(
        self,
        key: str,
        expected_error_context: ContextManager,
        user: User,
    ) -> None:
        """
        Ensure that when other emails do exist and verification is
        not required, the email is created with primary and verification
        as False, with an email confirmation.

        Args:
            key (str): confirmation key parameter.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            user (User): user fixture.
        """
        user.emails = [
            Email(address="test2@test.com", primary=True),
            Email(address="test3@test.com", primary=True),
        ]
        email_address = "test@test.com"

        with expected_error_context as error:
            user.email_create(
                address=email_address,
                max_emails=2,
                verification=True,
                email_confirmation_key=key,
            )

        if error is None:
            assert (
                len(user.emails) == 3
                and user.emails[2].address == email_address
                and user.emails[2].primary is False
                and user.emails[2].verified is False
                and user.emails[2].confirmation is not None
                and user.emails[0].primary is True
            )

    # ======================================
    # User.get_primary_email() tests
    # ======================================

    def test_get_primary_email_no_primary_email(self, user: User) -> None:
        """
        Ensure UserIntegrityError is raised if the user has no primary emails,
        as a User should always have at least one primary email.

        Args:
            user (User): user factory fixture.
        """

        user.emails = [Email(address="abc@abc.com", primary=False)]

        with pytest.raises(exceptions.UserIntegrityError):
            user.get_primary_email()

    def test_get_primary_email_success(self, user: User) -> None:
        """
        Ensure the primary email set on the user is returned.

        Args:
            user (User): user factory fixture.
        """

        primary_email = Email(address="primary@abc.com", primary=True)

        user.emails = [Email(address="abc@abc.com", primary=False), primary_email]

        assert user.get_primary_email() == primary_email

    # ======================================
    # User.email_confirmation_create() tests
    # ======================================

    def test_email_confirmation_create(self, user: User, mocker: MockerFixture) -> None:
        """
        Ensure the specified email is replaced with the result of
        email.new_confirmation.

        Args:
            user (User): user factory fixture.
            mocker (MockerFixture): pytest-mock.
        """
        mocker.patch(
            "src.domain.user.values.Email.new_confirmation",
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

        user.email_confirmation_create(address="test2@test.com", key="abc")

        assert user.emails == expected_result

    # ======================================
    # User.email_confirmation_confirm() tests
    # ======================================

    def test_email_confirmation_confirm(
        self, user: User, mocker: MockerFixture
    ) -> None:
        """
        Ensure the correct user sub-functions are called:
            - _get_email_by_confirmation_key() to retrieve the correct email.
            - Email.check_confirmation_expired() to block against expired
                email confirmation keys.
            - Email.verify() to verify the email.
            - _set_primary_email() to set the newly confirmed email as primary.
            - _trim_oldest_emails() to ensure the user does not have more
                emails than allowed.

        Args:
            user (User): user factory fixture.
            mocker (MockerFixture): pytest-mock.
        """
        mock_unverified_email = mocker.MagicMock(spec=Email)
        mock__get_email_by_confirmation_key = mocker.patch.object(
            user, "_get_email_by_confirmation_key", return_value=mock_unverified_email
        )
        mock_verified_email = mocker.MagicMock(spec=Email)
        mock_unverified_email.verify.return_value = mock_verified_email
        mock__set_primary_email = mocker.patch.object(user, "_set_primary_email")
        mock__trim_oldest_emails = mocker.patch.object(user, "_trim_oldest_emails")

        user.email_confirmation_confirm(key="abc", max_emails=0)

        mock__get_email_by_confirmation_key.assert_called_once_with(key="abc")
        mock_unverified_email.check_confirmation_expired.assert_called_once()
        mock_unverified_email.verify.assert_called_once()
        mock__set_primary_email.assert_called_once_with(mock_verified_email)
        mock__trim_oldest_emails.assert_called_once()

    # ======================================
    # User.set_password() tests
    # ======================================

    @pytest.mark.parametrize(
        ("existing_password", "password", "overwrite", "expected_error_context"),
        [
            # Test case: no existing password -> no error
            (None, "TestPassword", False, None),
            # Existing password -> error
            (
                "ExistingPassword",
                "TestPassword",
                False,
                exceptions.PasswordAlreadySetError,
            ),
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
        """
        Ensure the password is set, and error is raised if
        password already exists and overwrite is not specified.

        Args:
            existing_password (str): pre-existing user password.
            password (str): new password.
            overwrite (bool): explicit password overwrite permission.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            user (User): user object to test on (pytest fixture).
            mock_password_crypt (AbstractPasswordCrypt): (pytest fixture).
        """
        user._password_hash = existing_password

        with expected_error_context as error:
            await user.set_password(
                password=password,
                password_crypt=mock_password_crypt,
                overwrite=overwrite,
            )
            if error is None:
                assert user._password_hash == f"{password}::hash"

    # ======================================
    # User.password_reset_create() tests
    # ======================================

    def test_password_reset_create(self, user: User) -> None:
        """
        Ensure the password reset is added to the user object.

        Args:
            user (User): user factory fixture.
        """
        user.password_reset_confirmation = None
        key = "abc"

        user.password_reset_create(key=key)

        assert user.password_reset_confirmation.key == key

    # ======================================
    # User.password_reset_confirm() tests
    # ======================================

    async def test_password_reset_confirm_invalid_user_id(
        self, user: User, mocker: MockerFixture
    ) -> None:
        """
        Ensure that a PasswordResetConfirmationNotValid exception is raised
        when the the provided user_id does not match the User.

        Args:
            user (User): User fixture.
            mocker (MockerFixture): pytest-mock
        """
        user.id = 1
        user_id = user.id + 1
        key = "abc"
        new_password = "new_password"
        mock_password_crypt = mocker.Mock(spec=AbstractPasswordCrypt)
        user.password_reset_confirmation = PasswordResetConfirmation(key=key)
        expected_error_context = pytest.raises(
            exceptions.PasswordResetConfirmationNotValid
        )

        with expected_error_context:
            await user.password_reset_confirm(
                user_id=user_id,
                key=key,
                new_password=new_password,
                password_crypt=mock_password_crypt,
            )

    async def test_password_reset_confirm_password_reset_confirmation_not_found(
        self, user: User, mocker: MockerFixture
    ) -> None:
        """
        Ensure that a PasswordResetConfirmationNotFound exception is raised
        when the method is called on a User with password_reset_confirmation = None

        Args:
            user (User): User fixture
            mocker (MockerFixture): pytest-mock
        """
        user.id = 1
        user_id = user.id
        key = "abc"
        new_password = "new_password"
        mock_password_crypt = mocker.Mock(spec=AbstractPasswordCrypt)
        user.password_reset_confirmation = None
        expected_error_context = pytest.raises(
            exceptions.PasswordResetConfirmationNotFound
        )

        with expected_error_context:
            await user.password_reset_confirm(
                user_id=user_id,
                key=key,
                new_password=new_password,
                password_crypt=mock_password_crypt,
            )

    async def test_password_reset_confirm_invalid_key(
        self, user: User, mocker: MockerFixture
    ) -> None:
        """
        Ensure that a PasswordResetConfirmationNotValid exception is raised
        when the provided key does not match the existing PasswordResetConfirmation.

        Args:
            user (User): User fixture.
            mocker (MockerFixture): pytest-mock.
        """
        user.id = 1
        user_id = user.id
        key = "abc"
        new_password = "new_password"
        mock_password_crypt = mocker.Mock(spec=AbstractPasswordCrypt)
        user.password_reset_confirmation = PasswordResetConfirmation(key=key + "def")
        expected_error_context = pytest.raises(
            exceptions.PasswordResetConfirmationNotValid
        )

        with expected_error_context:
            await user.password_reset_confirm(
                user_id=user_id,
                key=key,
                new_password=new_password,
                password_crypt=mock_password_crypt,
            )

    async def test_password_reset_confirm_success(
        self, user: User, mocker: MockerFixture
    ) -> None:
        """
        Ensure that a the user's password is set to the new hashed password
        and the user's PasswordResetConfirmation is set to None.

        Args:
            user (User): User fixture.
            mocker (MockerFixture): pytest-mock.
        """
        user.id = 1
        user_id = user.id
        key = "abc"
        new_password = "new_password"
        hashed_new_password = "new_password::hash"
        mock_password_crypt = mocker.Mock(spec=AbstractPasswordCrypt)
        mock_password_crypt.verify_password.return_value = True
        mock_password_crypt.get_password_hash.return_value = hashed_new_password
        user.password_reset_confirmation = PasswordResetConfirmation(key=key)

        await user.password_reset_confirm(
            user_id=user_id,
            key=key,
            new_password=new_password,
            password_crypt=mock_password_crypt,
        )

        assert user._password_hash == hashed_new_password
        assert user.password_reset_confirmation is None

    # ======================================
    # User.verify_password() tests
    # ======================================

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
        """
        Ensure the function compares the input with
        password hash correctly.

        Args:
            existing_password (str): existing user password.
            password (str): input for comparison.
            expected_result (bool): expected result of comparison.
            user (User): user object to test on (pytest fixture).
            mock_password_crypt (AbstractPasswordCrypt): (pytest fixture).
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

    # ======================================
    # User.is_verified() tests
    # ======================================

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
        """
        Ensure verified is True if at least one email
        is verified, False if not.

        Args:
            emails (List[Email]): emails to add on the user.
            expected_output (bool): expected user.verified output.
            user (User): user factory fixture.
        """
        user.emails = emails

        assert user.is_verified() == expected_output

    # ======================================
    # User.is_expired() tests
    # ======================================

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
        """
        Ensure the user is expired if and only if it is older
        than expiry time hours and is not verified.

        Args:
            now (datetime): mock datetime.now().
            created_at (datetime): user creation time.
            expiry_time_hours (int): application setting.
            verified (bool): mock verified flag on user.
            expected_result (bool): expected expiry check result.
            user (User): user factory fixture.
            mocker (MockerFixture): pytest-mock.
        """
        mock_datetime = mocker.patch("src.domain.user.entities.datetime")
        mock_datetime.now.return_value = now
        user.created_at = created_at
        mock_is_verified = mocker.patch.object(
            user, "is_verified", return_value=verified
        )

        assert user.is_expired(expiry_time_hours=expiry_time_hours) == expected_result
        mock_is_verified.assert_called_once()

    # ======================================
    # User._get_email_by_confirmation_key() tests
    # ======================================

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
                exceptions.EmailConfirmationKeyNotFound,
            ),
        ],
        indirect=["expected_error_context"],
    )
    def test__get_email_by_confirmation_key(
        self,
        emails: List[Email],
        key: str,
        expected_result: Email,
        expected_error_context: ContextManager,
        user: User,
    ) -> None:
        """
        Ensure the email with the confirmation key is
        found and returned, otherwise an error is raised.

        Args:
            emails (List[Email]): existing emails on he user.
            key (str): key to attempt search for.
            expected_result (Email): expected function return.
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py.
            user (User): user factory fixture.
        """
        user.emails = emails

        with expected_error_context as error:
            email = user._get_email_by_confirmation_key(key=key)
            if error is None:
                assert email == expected_result

    # ======================================
    # User._set_primary_email() tests
    # ======================================

    def test__set_primary_email(self, user: User, mocker: MockerFixture) -> None:
        """
        Ensure that the given email is make primary and inserted
        at the front of the email list, while all other emails
        are unprimary.

        Args:
            user (User): user factory fixture.
            mocker (MockerFixture): pytest-mock.
        """
        existing_primary_email = Email(address="test1@test.com", primary=True)
        existing_unprimary_email = Email(address="test2@test.com", primary=False)
        mocker.patch.object(
            Email,
            "make_unprimary",
            return_value=Email(address="test1@test.com", primary=False),
        )
        mocker.patch(
            "src.domain.user.values.Email.make_primary",
            return_value=Email(address="test2@test.com", primary=True),
        )
        user.emails = [existing_primary_email, existing_unprimary_email]

        user._set_primary_email(existing_unprimary_email)

        assert user.emails == [
            Email(address="test2@test.com", primary=True),
            Email(address="test1@test.com", primary=False),
        ]

    # ======================================
    # User._trim_oldest_emails() tests
    # ======================================

    def test__trim_oldest_emails(self, user: User) -> None:
        """
        Ensure the oldest emails over max emails removed.
        and email list order is preserved.

        Args:
            user (User): user factory fixture.
        """
        max_emails = 2
        user.emails = [
            Email(address="test1@test.com", verified_at=datetime(2024, 1, 1, 1, 1)),
            Email(address="test2@test.com", verified_at=datetime(2023, 1, 1, 1, 1)),
            Email(address="test3@test.com", verified_at=datetime(2025, 1, 1, 1, 1)),
        ]

        user._trim_oldest_emails(max_emails)

        assert user.emails == [
            Email(address="test1@test.com", verified_at=datetime(2024, 1, 1, 1, 1)),
            Email(address="test3@test.com", verified_at=datetime(2025, 1, 1, 1, 1)),
        ]
