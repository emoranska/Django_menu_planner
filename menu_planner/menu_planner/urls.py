"""menu_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from backend.views import BaseView, signup, AllRecipeView, UserRecipeView, \
    RecipeAddIngredientsView, RecipeView, AllShoppingListsView, DeleteRecipeView, DeleteShoppingListView, UserPanelView, \
    AddRecipeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/log_out.html"), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html', success_url="/password_change_done/"), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_ok.html"), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="registration/reset_password.html", email_template_name="registration/reset_password_email.html",
        success_url="/password_reset_done/"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="registration/reset_password_done.html"), name='password_reset_done'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^signup/$', signup, name='signup'),

    path('menuplanner/', AllRecipeView.as_view(), name='recipes'),
    path('menuplanner/<int:id>/', UserRecipeView.as_view(), name='user_recipes'),
    path('menuplanner/<int:id>/add_ingredients/', RecipeAddIngredientsView.as_view(), name='add_ingredients'),
    path('menuplanner/recipe/<int:id>/', RecipeView.as_view(), name='recipe_view'),
    path('menuplanner/shoppinglists/<int:id>/', AllShoppingListsView.as_view(), name='shopping_lists'),
    path('menuplanner/recipe/<int:id>/delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
    path('menuplanner/shoppinglist/<int:id>/delete/', DeleteShoppingListView.as_view(), name='delete_shoppinglist'),
    path('menuplanner/user_panel/', UserPanelView.as_view(), name='user_panel'),
    path('menuplanner/add_recipe/', AddRecipeView.as_view(),name='add_recipe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
