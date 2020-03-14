from django.contrib.auth.models import User
from django.db import models


CATEGORIES = (
             ("alcohol", "alcohol"),
             ("bread", "bread"),
             ("concentrates", "concentrates"),
             ("dairy", "dairy"),
             ("drinks and liquids", "drinks and liquids"),
             ("meats and fishes", "meat and fishes"),
             ("others", "others"),
             ("powdered products", "powdered products"),
             ("spices", "spices"),
             ("sweets", "sweets"),
             ("vegetables and fruits", "vegetables and fruits")
              )


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64, choices=CATEGORIES)
    unit = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.name}, {self.unit}'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    add_date = models.DateField(auto_now=True)
    ingredients = models.ManyToManyField(Product, related_name="recipe", through="RecipeIngredients")
    description = models.TextField(verbose_name='steps')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.ingredient.__str__()


class ShoppingList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=64)
    create_date = models.DateField(auto_now=True)
    products = models.ManyToManyField(Product, related_name="shopping_list", through="ShoppingListProducts")


class ShoppingListProducts(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
