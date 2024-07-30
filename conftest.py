import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

HOST = "https://dev.qosyl.kz/api"
@pytest.fixture(autouse=True, scope="session")
def init_environment():

    response = requests.post(
        url=f"{HOST}/user/login",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}",
                 "Token": os.getenv('TOKEN_ID')}
    )


    assert response.status_code == 200