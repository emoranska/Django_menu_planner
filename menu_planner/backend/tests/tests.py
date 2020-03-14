import pytest
from django.contrib.auth.models import User

from backend.forms import SignUpForm


@pytest.mark.django_db
def test_login(client, set_up):
    response = client.post('/login/', {'username': 'john', 'password': 'smith'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_recipe_list(client, set_up):
    response = client.get('/menuplanner/')
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_get_recipe_detail(client, set_up):
#     response = client.get('/menuplanner/recipe/1/')
#     assert response.status_code == 200
#     for field in ("name", "add_date", "ingredients", "description", "author"):
#         assert field in response.data

#
# @pytest.mark.django_db
# def test_get_shoppinglists(client, set_up):
#     user = User.objects.get(id=1)
#     response = client.get(f'/menuplanner/shoppinglists/{user.id}/')
#     assert response.status_code == 200




# @pytest.mark.django_db
# def test_change_passwd_false():
#     # form_data = {'password1': '#3AdcTu', 'password2': '#3Au'}
#     form = SignUpForm(password1='#3AdcTu', password2='#3Au')
#     assert False == form.is_valid()
