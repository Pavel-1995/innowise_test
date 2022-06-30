import pytest

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.response import Response


class RegistrationTestCase(APITestCase):
    """Checking registration"""
    @pytest.mark.django_db
    def test_user_create(self):
        User.objects.create_user("user", "user@mail.com", "password")
        assert User.objects.count() == 1


class SigninTest(APITestCase):
    """Here we are testing the login function."""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test1", password="test1", email="test1@ex.com"
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username="test1", password="test1")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username="wrong", password="test1")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username="test", password="wrong")
        self.assertFalse(user is not None and user.is_authenticated)


class SignInViewTest(APITestCase):
    """Test Request and Response"""
    def test_1_post(self):
        factory = APIRequestFactory()
        request = factory.post(
            "http://127.0.0.1:8000/api/ticket/",
            json={"text_ticket": "dont work", "user": "test", "status": 1},
        )
        self.assertEqual(Response.status_code, status.HTTP_200_OK)

    def test_2_update(self):
        client = APIClient()
        client.login(username="pavel", password="12345678")
        request = client.put("http://127.0.0.1:8000/api/ticket/", json={"status": 2})
        self.assertEqual(Response.status_code, status.HTTP_200_OK)
