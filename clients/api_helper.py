import requests
from config import Config


class ApiPetStore:

    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def create_pet(self, data):
        method = '/pet'
        url = self.url + method

        response = requests.post(url, headers=self.default_headers, json=data)

        return response

    def get_pet_by_id(self, pet_id):
        method = f'/pet/{pet_id}'
        url = self.url + method

        response = requests.get(url, headers=self.default_headers)

        return response
