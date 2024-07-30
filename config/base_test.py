from services.schedule_meetings.api_schedule_meetings import ScheduleMeetingsAPI
from services.messages.api_messages import MessagesAPI


class BaseTest():

    def setup_method(self):
        self.api_schedule_meetings = ScheduleMeetingsAPI()
        self.api_messages = MessagesAPI()

