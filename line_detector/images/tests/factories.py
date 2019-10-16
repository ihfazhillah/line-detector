import factory
from django.core.files.base import ContentFile
from factory import DjangoModelFactory, Faker

from ..models import Image


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    title = Faker("sentence")
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
            "example.jpg",
        )
    )
