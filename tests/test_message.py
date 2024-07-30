import allure
from config.base_test import BaseTest
import pytest


@allure.feature("User messages")
class TestUserMessages(BaseTest):
    @pytest.mark.debug
    @allure.title("Get user dialogs")
    def test_get_user_dialogs(self):

        self.api_messages.get_user_dialogs()