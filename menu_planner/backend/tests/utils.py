from django.contrib.auth.models import User
from faker import Faker

from backend.models import Recipe, Product, RecipeIngredients

faker = Faker("pl_PL")

#
# def create_fake_recipe():
#     user = User.objects.get(username='test_user')
#     recipe = Recipe.objects.create(name=faker.name(), add_date='2020-03-14', description='bleble',
#                                    author=user)
#     return recipe
