import json

import pytest
from django.urls import reverse

from wanna_api.app import _HOME_MESSAGE


@pytest.mark.django
def test_app_home(client):
    url = reverse("home")
    response = client.get(url)

    assert response.status_code == 200
    content = json.loads(response.content.decode())
    assert content["message"] == _HOME_MESSAGE
