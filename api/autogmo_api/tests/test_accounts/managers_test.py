import copy

import pytest
from django.contrib.auth import get_user_model

from apps.accounts.managers import UserManager


class TestUserManager:
    def test_copy(self):
        """
        Test the creation of a shallow copy
        """
        manager = UserManager()
        manager_copy = copy.copy(manager)
        assert manager_copy is not None

    @pytest.mark.django_db
    def test_create_user(self):
        """
        Test the create_user function
        Requirements:
        Require email, username, and password as inputs
        Apply email normalization
        Set the kwargs of is_active, is_staff, and is_superuser to
        the correct defaults
        """

        User = get_user_model()
        user = User.objects.create_user(
            email="test@TEST.com", username="test", password="foo"
        )

        assert user.email == "test@test.com"
        assert user.username == ("test")
        assert str(user) == "test@test.com"
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False

        with pytest.raises(TypeError):
            User.objects.create_user()
        with pytest.raises(TypeError):
            User.objects.create_user(email="")
        with pytest.raises(TypeError):
            User.objects.create_user(email="", username="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="", username="", password="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="test", username="", password="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="test", username="test", password="")

    @pytest.mark.django_db
    def test_create_superuser(self):
        """
        Test the create_superuser function
        Requirements:
        Require email, username, and password as non-None inputs
        Apply email normalization
        Set the kwargs of is_active, is_staff, and  is_superuser to
        the correct defaults
        """

        User = get_user_model()
        superuser = User.objects.create_superuser(
            email="test@TEST.com", username="test", password="foo"
        )

        assert superuser.email == "test@test.com"
        assert superuser.username == "test"
        assert str(superuser) == "test@test.com"
        assert superuser.is_active is True
        assert superuser.is_staff is True
        assert superuser.is_superuser is True

        with pytest.raises(TypeError):
            User.objects.create_user()
        with pytest.raises(TypeError):
            User.objects.create_user(email="")
        with pytest.raises(TypeError):
            User.objects.create_user(email="", username="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="", username="", password="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="test", username="", password="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="test", username="test", password="")

        with pytest.raises(ValueError):
            User.objects.create_superuser(
                email="test@test.com",
                username="test",
                password="foo",
                is_superuser=False,
            )
        with pytest.raises(ValueError):
            User.objects.create_superuser(
                email="test@test.com", username="test", password="foo", is_staff=False
            )
