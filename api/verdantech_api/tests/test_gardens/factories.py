import factory

from verdantech_api.apps.gardens.models import Garden

from ..test_accounts.factories import UserFactory


class BaseGardenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Garden

    name = factory.Faker("first_name")
    string_id = factory.Faker("slug")
    visibility = "PRIVATE"


class ValidGardenFactory(BaseGardenFactory):

    admins = factory.RelatedFactory(UserFactory, factory_related_name="admin_gardens")
