import factory
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("username")
    password = factory.Faker("password", length=12)
