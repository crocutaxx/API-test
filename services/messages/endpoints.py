from conftest import HOST


# Define endpoints for Dialogs API here
class Endpoints:

    get_user_dialogs = f"{HOST}/user/getDialogs"
    # edit_meeting = lambda self, meet_id: f"{HOST}/schedule-meeting/{meet_id}"