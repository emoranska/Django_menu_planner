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

#
# @pytest.fixture
# def set_up():
#     User.objects.create_user(username='test_user', email='test@test.com', password='top_secret')
#     Product.objects.create(name='egg', category='diary', unit='amount')
#     create_fake_recipe()