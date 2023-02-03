import pytest
from model_bakery import baker


class LoginViewTest:
    @pytest.mark.django_db
    def test_login():
        pass

    def test_csrf():
        pass
