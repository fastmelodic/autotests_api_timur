import string
import pytest
from random import choice

from schemas.general import schemas


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


def test_update_pet(base_fixture, pet_id):

    name = ''.join(choice(string.ascii_lowercase) for i in range(5))
    category = ''.join(choice(string.ascii_lowercase) for i in range(7))
    status = choice(['available', 'pending', 'sold'])
    photo_url = 'http://' + ''.join(choice(string.ascii_lowercase) for i in range(5)) + '.com'
    tag = ''.join(choice(string.ascii_lowercase) for i in range(5))
    data = base_fixture.helper.gen_update_pet_req(pet_id, name, category, status, photo_url, tag)

    response_update_pet = base_fixture.api.update_pet(data)

    response_get_pet = base_fixture.api.get_pet_by_id(pet_id)
    resp_tag = None
    for i in response_get_pet.json()['tags']:
        if i['testKey']:
            resp_tag = ['testKey']
            break

    assert response_update_pet.status_code == 200, response_update_pet.text
    base_fixture.checker.validate_json(response_update_pet.json(), 'get_pet_by_id')
    assert response_get_pet.json()['name'] == name
    assert response_get_pet.json()['status'] == status
    assert resp_tag == tag
    assert photo_url in response_get_pet.json()['photoUrls']
    assert response_get_pet.json()['category']['testKey'] == category


def test_required_fields_check_create_pet_ver1(base_fixture):

    name = ''.join(choice(string.ascii_lowercase) for i in range(5))
    category = ''.join(choice(string.ascii_lowercase) for i in range(7))
    status = choice(['available', 'pending', 'sold'])
    data = base_fixture.helper.gen_create_pet_req(name, category, status)
    base_fixture.helper.delete_required_fields(data, 'get_pet_by_id')

    response = base_fixture.api.create_pet(data)

    assert response.status_code == 422, response.text


@pytest.mark.parametrize('required_field', schemas['get_pet_by_id']['required'])
def test_required_fields_check_create_pet_ver2(base_fixture, required_field):

    name = ''.join(choice(string.ascii_lowercase) for i in range(5))
    category = ''.join(choice(string.ascii_lowercase) for i in range(7))
    status = choice(['available', 'pending', 'sold'])
    data = base_fixture.helper.gen_create_pet_req(name, category, status)
    data.pop(required_field)

    response = base_fixture.api.create_pet(data)

    assert response.status_code == 422, response.text
