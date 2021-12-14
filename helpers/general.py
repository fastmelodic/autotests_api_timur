import string
from random import choice


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
