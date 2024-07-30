import requests
import allure
from utils.helper import Helper
from services.messages.payloads import Payloads
from services.messages.endpoints import Endpoints
from config.headers import Headers
from services.messages.models.messages_model import *


class MessagesAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get user dialogs")
    def get_user_dialogs(self):

        response = requests.get(
            url=self.endpoints.get_user_dialogs,
            headers=self.headers.basic)

        assert response.status_code == 200, response.json()
        self.attach_respons(response.json())
        model = GetUserDialogs(root=response.json())

        return model