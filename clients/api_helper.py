import requests
from config import Config


class ApiPetStore:

    def __init__(self):
        self.url = Config.url
        self.headers = {'accept': 'application/json'}

    def create_user(self, data):
        url = self.url + '/user'
        return requests.post(url, headers=self.headers, json=data)

    def delete_user(self, username):
        url = self.url + f'/user/{username}'
        return requests.delete(url, headers=self.headers)

    def login(self, username, password):
        url = self.url + f'/user/login'
        params = {'username': username, 'password': password}
        return requests.get(url, headers=self.headers, params=params)

    def logout(self, session_id):
        url = self.url + f'/user/logout'
        data = {'session': session_id}
        return requests.get(url, headers=self.headers, json=data)

    def create_pet(self, data):
        url = self.url + '/pet'
        return requests.post(url, headers=self.headers, json=data)

    def get_pet_by_id(self, pet_id):
        url = self.url + f'/pet/{pet_id}'
        return requests.get(url, headers=self.headers)

    def update_pet(self, data):
        url = self.url + '/pet'
        return requests.put(url, headers=self.headers, json=data)
