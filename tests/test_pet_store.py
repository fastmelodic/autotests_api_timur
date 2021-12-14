import string
import pytest
from random import choice


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_create_pet(base_fixture, status):

    name = ''.join(choice(string.ascii_lowercase) for i in range(5))
    category = ''.join(choice(string.ascii_lowercase) for i in range(7))
    data = base_fixture.helper.gen_create_pet_req(name, category, status)

    response = base_fixture.api.create_pet(data)

    assert response.status_code == 200, response.text
    assert response.json()['name'] == name


def test_get_pet_by_id(base_fixture, pet_id):

    response = base_fixture.api.get_pet_by_id(pet_id)

    assert response.status_code == 200, response.text
    base_fixture.checker.validate_json(response.json(), 'get_pet_by_id')
    assert response.json()['id'] == pet_id, response.text
