import factory
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.Faker("password", length=12)
