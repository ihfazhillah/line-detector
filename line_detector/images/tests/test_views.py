import pytest
from django.urls import reverse
from .factories import ImageFactory


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

        data = {
            "title": "hello world",
            "scale": 1010
        }

        response = client.post(url, data)
        assert response.status_code == 302
