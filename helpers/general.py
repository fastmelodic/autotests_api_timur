import string
from random import choice

from schemas.general import schemas


class Helper:

    @staticmethod
    def gen_create_pet_req(name, category, status):

        data = {
            'category': {
                'name': category
            },
            'name': name,
            'photoUrls': [
                ''.join(choice(string.ascii_lowercase) for i in range(10))
            ],
            'tags': [
                {
                    'name': ''.join(choice(string.ascii_lowercase) for i in range(5))
                }
            ],
            'status': status
        }

        return data

    @staticmethod
    def gen_update_pet_req(pet_id, name, category, status, photo_url, tag):

        data = {
            'id': pet_id,
            'category': {
                'testKey': category
            },
            'name': name,
            'photoUrls': [
                photo_url
            ],
            'tags': [
                {
                   'testKey': tag
                }
            ],
            'status': status
        }

        return data

    @staticmethod
    def delete_required_fields(data, schema):
        fields_to_delete = schemas[schema]['required']
        for i in fields_to_delete:
            data.pop(i)

        return data
