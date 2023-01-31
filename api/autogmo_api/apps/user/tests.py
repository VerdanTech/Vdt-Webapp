from django.contrib.auth import get_user_model

from .managers import UserManager

# Testing the custom UserManager functions
def test_manager():
    """
    Test the creation of a shallow copy
    """
    manager = CustomUserManager()
    manager_copy = copy.copy(manager)
    self.assertIsNotNone(manager_copy)

def test_create_user():
    """
    Test the create_user function
    Requirements:
    Require email, username, and password as non-None inputs
    Apply email normalization
    Set the kwargs of is_active, is_staff, and is_superuser to
    the correct defaults
    """

    User = get_user_model()
    user = User.objects.create_user(
        email="test@TEST.com", username="test", password="foo"
    )

    self.assertEqual(user.email, "test@test.com")
    self.assertEqual(user.username, "test")
    self.assertEqual(str(user), "test@test.com")
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)

    with self.assertRaises(TypeError):
        User.objects.create_user()
    with self.assertRaises(TypeError):
        User.objects.create_user(email="")
    with self.assertRaises(TypeError):
        User.objects.create_user(email="", username="")
    with self.assertRaises(ValueError):
        User.objects.create_user(email="", username="", password="")
    with self.assertRaises(ValueError):
        User.objects.create_user(email="test", username="", password="")
    with self.assertRaises(ValueError):
        User.objects.create_user(email="test", username="test", password="")
