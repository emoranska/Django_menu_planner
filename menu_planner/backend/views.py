from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from backend.forms import SignUpForm, AddRecipeForm, AddShoppingListForm, RecipeAddIngredientsForm
from backend.models import Recipe, ShoppingList, ShoppingListProducts, RecipeIngredients, Product


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class AllRecipeView(View):
    def get(self, request):
        form = AddRecipeForm()
        recipes = Recipe.objects.all()
        user = request.user
        return render(request, 'all-recipes.html', {"form": form, "recipes": recipes, "user": user})

    def post(self, request):
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save()
            url = reverse('add_ingredients', kwargs={'id': new_recipe.id})
            return HttpResponseRedirect(url)


class RecipeAddIngredientsView(LoginRequiredMixin, View):
    def get(self, request, id):
        form = RecipeAddIngredientsForm()
        products = Product.objects.all()
        recipe = Recipe.objects.get(pk=id)
        return render(request, 'recipe-ingredients-form.html', {"form": form, "recipe": recipe,
                                                                "products": products})

    def post(self, request, id):
        form = RecipeAddIngredientsForm(request.POST)
        recipe = Recipe.objects.get(pk=id)
        products = Product.objects.all()

        if form.is_valid():
            form.save()
            url = reverse('add_ingredients', kwargs={'id': id})
            return HttpResponseRedirect(url)

        return render(request, 'recipe-ingredients-form.html', {"form": form, "recipe": recipe, "products": products})


class RecipeView(LoginRequiredMixin, View):
    def get(self, request, id):
        form = AddShoppingListForm()
        recipe = Recipe.objects.get(pk=id)
        ingredients = RecipeIngredients.objects.filter(recipe_id=id)
        user = request.user
        return render(request, 'recipe-view.html', {"form": form, "recipe": recipe, "ingredients": ingredients,
                                                    "user": user})

    def post(self, request, id):
        form = AddShoppingListForm(request.POST)
        if form.is_valid():
            new_shoppinglist = form.save()
            recipe_ingredients = RecipeIngredients.objects.filter(recipe_id=id)

            for ingredient in recipe_ingredients:
                products = Product.objects.filter(id=ingredient.ingredient_id)
                for product in products:
                    ShoppingListProducts.objects.create(shopping_list=new_shoppinglist,
                                                        product=product, quantity=ingredient.quantity)
            return render(request, 'recipe-shopping-list.html', {"new_shoppinglist": new_shoppinglist,
                                                                 "items": recipe_ingredients})


class UserRecipeView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        recipes = Recipe.objects.filter(author=user)
        return render(request, 'user-recipes.html', {"recipes": recipes})


class AllShoppingListsView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        shopping_lists = ShoppingList.objects.filter(author=user)

        for shopping_list in shopping_lists:
            shopping_list.ingredients = ShoppingListProducts.objects.filter(shopping_list=shopping_list)

        return render(request, 'user-shoppinglists.html', {"shopping_lists": shopping_lists})


class DeleteRecipeView(LoginRequiredMixin, View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        return render(request, 'recipe_confirm_delete.html', {"recipe": recipe})

    def post(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        recipe.delete()
        user = request.user
        return HttpResponseRedirect(reverse('user_recipes', kwargs={'id': user.id}))


class DeleteShoppingListView(LoginRequiredMixin, View):
    def get(self, request, id):
        shopping_list = ShoppingList.objects.get(pk=id)
        return render(request, 'shoppinglist_confirm_delete.html', {"shopping_list": shopping_list})

    def post(self, request, id):
        shopping_list = ShoppingList.objects.get(pk=id)
        shopping_list.delete()
        user = request.user
        return HttpResponseRedirect(reverse('shopping_lists', kwargs={'id': user.id}))
