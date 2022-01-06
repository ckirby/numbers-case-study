import json
from django.urls import reverse

from humanize import errors


class TestHumanizeView:
    def test_good_get(self, client):
        url = reverse("humanize")
        response = client.get(f"{url}?number=1234")
        data = json.loads(response.content)
        assert data["status"] == "ok"
        assert data["num_in_english"] == "one thousand two hundred thirty four"

    def test_get_without_param(self, client):
        url = reverse("humanize")
        response = client.get(url)
        data = json.loads(response.content)
        assert data["status"] == f"Error: {errors.ERRORS['GET']['REQUIRED']}"

    def test_get_with_non_integer_param(self, client):
        url = reverse("humanize")
        response = client.get(f"{url}?number=1234.2")
        data = json.loads(response.content)
        assert data["status"] == f"Error: {errors.ERRORS['GET']['INVALID']}"

        response = client.get(f"{url}?number=blah")
        data = json.loads(response.content)
        assert data["status"] == f"Error: {errors.ERRORS['GET']['INVALID']}"

    def test_good_post(self, client):
        url = reverse("humanize")
        response = client.post(url, {"number": 1234})
        data = json.loads(response.content)
        assert data["status"] == "ok"
        assert data["num_in_english"] == "one thousand two hundred thirty four"

    def test_good_post_with_integer_as_string(self, client):
        url = reverse("humanize")
        response = client.post(url, {"number": "1234"})
        data = json.loads(response.content)
        assert data["status"] == "ok"
        assert data["num_in_english"] == "one thousand two hundred thirty four"

    def test_post_with_non_integer_param(self, client):
        url = reverse("humanize")
        response = client.post(url, {"number": 1234.2})
        data = json.loads(response.content)
        assert data["status"] == f"Error: {errors.ERRORS['POST']['INVALID']}"

        url = reverse("humanize")
        response = client.post(url, {"number": "blah"})
        data = json.loads(response.content)
        assert data["status"] == f"Error: {errors.ERRORS['POST']['INVALID']}"

    def test_post_without_param(self, client):
        url = reverse("humanize")
        response = client.post(url)
        data = json.loads(response.content)
        assert data["status"] == f"Error: {errors.ERRORS['POST']['REQUIRED']}"
