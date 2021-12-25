import pytest
import string
from random import choice
from application import Application


@pytest.fixture(scope="session")
def base_fixture():
    """
    Инициализация:
    1. Создаем юзера
    2. Логинимся под созданным юзером
    3. Прокидываем сессию в заголовки

    Финализация:
    1. логаут
    2. удаляем юзера
    """
    fixture = Application()
    username = ''.join(choice(string.ascii_lowercase) for i in range(7))
    password = ''.join(choice(string.ascii_lowercase) for i in range(7))
    user_data = {'username': username, 'password': password}
    fixture.api.create_user(user_data)
    login_response = fixture.api.login(username, password)
    session_id = login_response.json()['message'][23:]
    fixture.api.headers.update({'session': session_id})

    yield fixture

    fixture.api.logout(session_id)
    fixture.api.delete_user(username)


@pytest.fixture()
def pet_id():

    name = ''.join(choice(string.ascii_lowercase) for i in range(5))
    category = ''.join(choice(string.ascii_lowercase) for i in range(7))
    status = choice(['available', 'pending', 'sold'])
    data = base_fixture.helper.gen_create_pet_req(name, category, status)

    response = base_fixture.api.create_pet(data)

    return response.json()['id']
