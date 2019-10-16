import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .factories import ImageFactory
from .helpers import create_image

pytestmark = pytest.mark.django_db


class TestImage:
    def test_list(self, client):
        ImageFactory.create_batch(3)
        url = reverse("images:list")
        response = client.get(url)
        assert response.status_code == 200

    def test_detail(self, client):
        image = ImageFactory()
        url = reverse("images:detail", args=[image.id])
        response = client.get(url)
        assert response.status_code == 200

    def test_create(self, client):
        url = reverse("images:create")
        response = client.get(url)

        assert response.status_code == 200

        image = create_image(None, "line.png")
        image = SimpleUploadedFile("line.png", image.getvalue())
        data = {"title": "hello world", "scale": 1010, "image": image, "options": "[]"}

        response = client.post(url, data)
        assert response.status_code == 302
