from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from backend.models import Recipe, ShoppingList, RecipeIngredients


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddRecipeForm(ModelForm):
     class Meta:
         model = Recipe
         exclude = ['add_date', 'ingredients']


class RecipeAddIngredientsForm(ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = '__all__'


class AddShoppingListForm(ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['name', 'author']
