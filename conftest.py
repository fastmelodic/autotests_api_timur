import pytest
import string
from random import choice
from application import Application


fixture = Application()


@pytest.fixture(scope="session")
def base_fixture():
    return fixture


@pytest.fixture()
def pet_id():

    name = ''.join(choice(string.ascii_lowercase) for i in range(5))
    category = ''.join(choice(string.ascii_lowercase) for i in range(7))
    status = choice(['available', 'pending', 'sold'])
    data = fixture.helper.gen_create_pet_req(name, category, status)

    response = fixture.api.create_pet(data)

    return response.json()['id']
