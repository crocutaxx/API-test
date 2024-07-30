import requests
import allure
from utils.helper import Helper
from services.schedule_meetings.payloads import Payloads
from services.schedule_meetings.endpoints import Endpoints
from config.headers import Headers
from services.schedule_meetings.models.schedule_meetings_model import *


class ScheduleMeetingsAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create meeting")
    def create_meeting(self):

        response = requests.post(
            url=self.endpoints.create_meeting,
            headers=self.headers.basic,
            data=self.payloads.create_meeting())

        assert response.status_code == 201, response.json()
        self.attach_respons(response.json())
        model = CreateNewMeeting(**response.json())

        return model

    @allure.step("Get meeting by meet ID")
    def get_meeting_by_id(self, meet_id):
        response = requests.get(
            url=self.endpoints.get_meeting_by_id(meet_id),
            headers=self.headers.basic)

        assert response.status_code == 200, response.json()
        self.attach_respons(response.json())
        model = GetMeetingByMeetId(**response.json())

        return model
