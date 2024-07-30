from faker import Faker
from datetime import datetime
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Payloads():

    def create_meeting(self):
        fake = Faker()

        with open("data/tests_data.json", "r") as json_file:
            data = json.load(json_file)
            self.user_id= str(data["userId"])

        current_datetime = datetime.now()
        current_date = current_datetime.date()


        data = {
            'topic': f"Test topic {fake.domain_word()}",
            'date': current_date.strftime('%Y-%m-%d'),
            'time': '11:32',
            "durationMinute": str(fake.random.randint(1, 300)),
            "speakerVideo": 'false',
            "speakerAudio": 'false',
            "membersVideo": 'false',
            "membersAudio": 'false',
            "waitingHall": 'false',
            "calendar": '1',
            "template": '4',
            "members": '[{"id":'+self.user_id+',"speaker":true}]'
        }
        body = MultipartEncoder(fields=data, boundary='--------------------------899774804080388235181464')

        return body, body.content_type
