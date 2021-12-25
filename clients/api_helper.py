import requests
from config import Config


class ApiPetStore:

    def __init__(self):
        self.url = Config.url
        self.headers = {'accept': 'application/json'}

    def create_user(self, data):
        url = self.url + '/user'
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def delete_user(self, username):
        url = self.url + f'/user/{username}'
        response = requests.delete(url, headers=self.headers)
        return response

    def login(self, username, password):
        url = self.url + f'/user/login'
        params = {'username': username, 'password': password}
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def logout(self, session_id):
        url = self.url + f'/user/logout'
        data = {'session': session_id}
        response = requests.get(url, headers=self.headers, json=data)
        return response

    def create_pet(self, data):
        url = self.url + '/pet'
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def get_pet_by_id(self, pet_id):
        url = self.url + f'/pet/{pet_id}'
        response = requests.get(url, headers=self.headers)
        return response
