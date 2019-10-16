from factory import DjangoModelFactory, Faker
from ..models import Image


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    title = Faker("sentence")
