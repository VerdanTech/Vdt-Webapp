from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    """User model manager class"""

    def _create_user(self, email: str, username: str, password: str, **kwargs) -> User:
        """Create and save new user with given username, email, and password

        Args:
            email (str): user email
            username (str): user username
            password (str): user password

        Raises:
            ValueError: Email must be set
            ValueError: Username must be set
            ValueError: Password must be set

        Returns:
            User: User model created in database
        """

        if not email:
            raise ValueError(_("Email must be set"))
        if not username:
            raise ValueError(_("Username must be set"))
        if not password:
            raise ValueError(_("Password must be set"))

        email = self.normalize_email(email)

        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email: str, username: str, password: str, **kwargs) -> User:
        """Create and save new user with given username, email, and password

        Args:
            email (str): user email
            username (str): user username
            password (str): user password

        Raises:
            ValueError: Email must be set
            ValueError: Username must be set
            ValueError: Password must be set

        Returns:
            User: User model created in database
        """

        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **kwargs)

    def create_superuser(
        self, email: str, username: str, password: str, **kwargs
    ) -> User:
        """Create and save new superuser with given username, email, and password

        Args:
            email (str): user email
            username (str): user username
            password (str): user password

        Raises:
            ValueError: Email must be set
            ValueError: Username must be set
            ValueError: Password must be set

        Returns:
            User: User model created in database
        """
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **kwargs)
