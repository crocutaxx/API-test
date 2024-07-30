from conftest import HOST


class Endpoints:
    create_meeting = f"{HOST}/schedule-meeting"
    get_meeting_by_id = lambda self, meet_id: f"{HOST}/schedule-meetings/{meet_id}"

