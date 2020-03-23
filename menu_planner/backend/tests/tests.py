import pytest

from backend.forms import SignUpForm


#################### USER TESTS ####################
from backend.models import Recipe


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
def test_register_user_existing_login(user):
    form_data = {'username': 'test_user',
                 'password1': '#asdA44as',
                 'password2': '#asdA44as',
                 'email': 'test@gmail.com'}
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
    assert response.url == '/'


@pytest.mark.django_db
def test_change_password(client):
    client.login(username='john', password='smith')
    response = client.post('/password_change/', {'old_password': 'smith', 'new_password1': 'nowak',
                                                'new_password2': 'nowak'})
    assert response.status_code == 302
    assert response.url == '/password_change_done/'


@pytest.mark.django_db
def test_create_recipe(client, user):
    recipe = Recipe.objects.create(name="Test_recipe", add_date='2020-03-14', description='whatever',
                                    author=user)
    assert recipe


@pytest.mark.django_db
def test_get_recipe_list(client):
    response = client.get('/menuplanner/')
    assert response.status_code == 200

