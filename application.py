from clients.api_helper import ApiPetStore
from helpers.general import Helper
from checkers.general import Checker


class Application:

    def __init__(self):

        self.api = ApiPetStore()
        self.helper = Helper()
        self.checker = Checker()
