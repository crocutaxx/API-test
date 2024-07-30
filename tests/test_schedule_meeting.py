import allure
from config.base_test import BaseTest
import pytest


@allure.feature("Schedule Meetings")
class TestScheduleMeetings(BaseTest):
    @allure.title("Create meeting")
    def test_create_meeting(self):

        try:
            meeting = self.api_schedule_meetings.create_meeting()
        finally:
            self.api_schedule_meetings.delete_meeting_by_id(meeting.id)

    @allure.title("Get meeting by id")
    def test_get_meeting_by_id(self):

        try:
            meeting = self.api_schedule_meetings.create_meeting()
            self.api_schedule_meetings.get_meeting_by_id(meeting.id)
        finally:
            self.api_schedule_meetings.delete_meeting_by_id(meeting.id)

