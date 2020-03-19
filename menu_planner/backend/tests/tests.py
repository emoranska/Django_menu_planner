import pytest

from backend.forms import SignUpForm


#################### USER TESTS ####################

@pytest.mark.django_db
def test_register_user_ok():
    form_data = {'username': 'testowy',
                 'email': 'test@.gmail.com',
                 'password1': '#asdA44as',
                 'password2': '#asdA44as'
                 }
    form = SignUpForm(data=form_data)
    assert False == form.is_valid()


@pytest.mark.django_db
def test_register_user_wrong_repeated_password():
    form_data = {'username': 'testowy',
                 'email': 'test@.gmail.com',
                 'password1': '#asdA44as',
                 'password2': 'A44as'
                 }
    form = SignUpForm(data=form_data)
    assert False == form.is_valid()


@pytest.mark.django_db
def test_register_user_wrong_mail():
    form_data = {'username': 'testowy',
                 'password1': '#asdA44as',
                 'password2': '#asdA44as',
                 'email': 'test.gmail.com'}
    form = SignUpForm(data=form_data)
    assert False == form.is_valid()


@pytest.mark.django_db
def test_register_user_existing_login():
    form_data = {'username': 'emi',
                 'password1': '#asdA44as',
                 'password2': '#asdA44as',
                 'email': 'test@.gmail.com'}
    form = SignUpForm(data=form_data)
    assert False == form.is_valid()


@pytest.mark.django_db
def test_login(client):
    response = client.post('/login/', {'username': 'john', 'password': 'smith'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout(client):
    client.login(username='john', password='smith')
    response = client.get('/logout/')
    assert response.status_code == 302

#
# @pytest.mark.django_db
# def test_change_password_true(client, set_up):
#     form_data = {'password1': '#3AdcTu', 'password2': '#3AdcTu'}
#     form = SignUpForm(data=form_data)
#     assert True == form.is_valid()
#
#
# def test_change_password_difference():
#     form_data = {'new_password': '#3AdcTu', 'new_password2': '#3Au'}
#     form = SignUpForm(data=form_data)
#     assert False == form.is_valid()
#
#
# @pytest.mark.django_db
# def test_get_recipe_list(client, set_up):
#     response = client.get('/menuplanner/')
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db
# def test_get_recipe_detail(client, set_up):
#     response = client.get('/menuplanner/recipe/1/', {})
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
