import os
import sys

from django.contrib.auth.models import User

sys.path.append(os.path.dirname(__file__))
from django.test import Client
from .utils import faker
import pytest

from backend.models import Product


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    user = User.objects.get()
    return user


@pytest.fixture
def set_up():
    for _ in range(5):
        Product.objects.create(name=faker.name(), category='dairy', unit='kg')