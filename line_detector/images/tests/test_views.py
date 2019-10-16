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
